variable "project" {
    default = "ForNewVoiceMedia"
}

variable "availability_zone" {
    default = "eu-west-1a"
}

variable "ami" {
    default = "ami-867ceaff"
}

variable "instance_type" {
    default = "t2.nano"
}

variable "left_cidr" {
    default = "10.0.1.0/24"
}

variable "right_cidr" {
    default = "10.0.2.0/24"
}

data "aws_caller_identity" "current" {
}
