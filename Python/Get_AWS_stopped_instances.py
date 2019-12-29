"""
Prerequisite - Aws cli needs to be configured first.
"""

import boto3

def get_name(tag):
    for reader in tag:
        if(reader.get('Key') == 'Name'):
            return(reader.get('Value'))
    return("Empty")

def getInstances(region_name):
    ec2 = boto3.resource('ec2', region_name=region_name)

    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }
    ]

    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)
    result = "Stopped instances in \""+region_name+"\" region\n\n"
    for i in instances:
        tags = i.tags
        name = get_name(tags)
        instance_id=i.id
        message = "Instance Name= {}   ---   Instance Id= {}".format(name, instance_id)+"\n"
        result += message

    return(result)

print(getInstances('ap-south-1'))
