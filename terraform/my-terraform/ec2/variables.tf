variable "ami_id" {
  type = string
  default = "name_of_ami"
}

variable "key_name" {
  type = string
  default = "name_of_key"
}

variable "instance_type" {
  type = string
  default = "t2.micro"
}

variable "associate_public_ip_address" {
  default = "false"
}

variable "inst_count" {
  default = "1"
}

variable "ebs_root_volume_type" {
  default = "gp2"
}

variable "ebs_root_volume_size" {
  default = "8"
}

variable "ebs_root_delete_on_termination" {
  default = "true"
}