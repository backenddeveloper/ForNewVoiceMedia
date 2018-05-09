resource "aws_flow_log" "left_flow_log" {
    log_group_name     = "${aws_cloudwatch_log_group.flow_log_group.name}"
    iam_role_arn       = "${aws_iam_role.flow_log_role.arn}"
    vpc_id             = "${aws_vpc.left_vpc.id}"
    traffic_type       = "ALL"

    tags {
        Name           = "${var.project}"
    }
}

resource "aws_flow_log" "right_flow_log" {
    log_group_name     = "${aws_cloudwatch_log_group.flow_log_group.name}"
    iam_role_arn       = "${aws_iam_role.flow_log_role.arn}"
    vpc_id             = "${aws_vpc.right_vpc.id}"
    traffic_type       = "ALL"

    tags {
        Name           = "${var.project}"
    }
}

resource "aws_cloudwatch_log_group" "flow_log_group" {
    name               = "flow_log_group"

    tags {
        Name           = "${var.project}"
    }
}

resource "aws_iam_role" "flow_log_role" {
    name               = "flow_log_role"
    
    assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "vpc-flow-logs.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

    tags {
        Name           = "${var.project}"
    }
}

resource "aws_iam_role_policy" "flow_log_policy" {
    name               = "flow_log_policy"
    role               = "${aws_iam_role.flow_log_role.id}"
    
    policy             = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF

    tags {
        Name           = "${var.project}"
    }
}
