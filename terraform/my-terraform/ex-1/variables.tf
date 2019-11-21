variable "test_var" {
    type = string
    default = "hello world!"
}

variable "author_name" {
    type = string
    default = "harshit sharma"
}

variable "author_info"{
    type = map(string)
    default = {
        name = "Harshit Sharma"
        age = "21"
        email = "sharma1612harshit@gmail.com"
    }
}

variable "devices" {
    type = list
    default = ["iphone", "macbook"]
}

#use variables -
//var.author_name or ${var.author_name}
//var.author_info.age
//var.devices[0]

#supplying variable values through cli -
//terraform apply -var="image_id=ami-abc123"
//terraform apply -var='image_id_list=["ami-abc123","ami-def456"]'
//terraform apply -var='image_id_map={"us-east-1":"ami-abc123","us-east-2":"ami-def456"}'