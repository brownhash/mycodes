# creating ec2

2terraform {
    required_version = ">=0.12.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ec2" {
    ami = var.ami_id
    key_name = var.key_name
    instance_type = var.instance_type
    associate_public_ip_address = var.associate_public_ip_address
    count = var.inst_count

    root_block_device {
        volume_type = var.ebs_root_volume_type
        volume_size = var.ebs_root_volume_size
        delete_on_termination = "true"
    }

    tags = {
        Name = "Harshit-testing-terraform",
        environment = "stag"
    }
}
