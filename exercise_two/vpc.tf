resource "aws_vpc" "left_vpc" {
    cidr_block                = "${var.left_cidr}"
    enable_dns_hostnames      = true
    enable_dns_support        = true

    tags {
        Name                  = "${var.project}"
    }
}

resource "aws_vpc" "right_vpc" {
    cidr_block                = "${var.left_cidr}"
    enable_dns_hostnames      = true
    enable_dns_support        = true

    tags {
        Name                  = "${var.project}"
    }
}

resource "aws_subnet" "left_vpc_subnet" {
    vpc_id                    = "${aws_vpc.left_vpc.id}"
    cidr_block                = "${var.left_cidr}"
    availability_zone         = "${var.availability_zone}"

    tags {
        Name                  = "${var.project}"
    }
}

resource "aws_subnet" "right_vpc_subnet" {
    vpc_id                    = "${aws_vpc.right_vpc.id}"
    cidr_block                = "${var.right_cidr}"
    availability_zone         = "${var.availability_zone}"

    tags {
        Name                  = "${var.project}"
    }
}

resource "aws_vpc_peering_connection" "the_vpn" {
    peer_owner_id             = "${data.aws_caller_identity.current.account_id}"
    peer_vpc_id               = "${aws_vpc.right_vpc.id}"
    vpc_id                    = "${aws_vpc.left_vpc.id}"
    auto_accept               = true

    tags {
        Name                  = "${var.project}"
    }
}

resource "aws_route" "left_to_right" {
    route_table_id            = "${aws_vpc.left_vpc.main_route_table_id}"
    destination_cidr_block    = "${aws_vpc.right_vpc.cidr_block}"
    vpc_peering_connection_id = "${aws_vpc_peering_connection.the_vpn.id}"

    tags {
        Name                  = "${var.project}"
    }
}

resource "aws_route" "right_to_left" {
    route_table_id            = "${aws_vpc.right_vpc.main_route_table_id}"
    destination_cidr_block    = "${aws_vpc.left_vpc.cidr_block}"
    vpc_peering_connection_id = "${aws_vpc_peering_connection.the_vpn.id}"

    tags {
        Name                  = "${var.project}"
    }
}

resource "aws_security_group" "both_directions" {
    description               = "Default security group for all instances in VPC ${aws_vpc.primary.id}"
    vpc_id                    = "${aws_vpc.primary.id}"
    
    ingress {
      from_port               = 0
      to_port                 = 0
      protocol                = "-1"
      cidr_blocks             = [
        "${aws_vpc.right_vpc.cidr_block}",
        "${aws_vpc.left_vpc.cidr_block}"
      ]
    }
    
    egress {
      from_port               = 0
      to_port                 = 0
      protocol                = "-1"
      cidr_blocks             = [
        "${aws_vpc.right_vpc.cidr_block}",
        "${aws_vpc.left_vpc.cidr_block}"
      ]
    }

    tags {
        Name                  = "${var.project}"
    }
}
