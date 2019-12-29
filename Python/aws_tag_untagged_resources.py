import boto3
import time


# this function accepts the region and id of a particular volume
# returns tags attached to that volume if any else returns None
def describe_volume_tags(region_name, volume_id):
    client = boto3.client('ec2', region_name=region_name)
    response = client.describe_volumes(
        VolumeIds=[
            volume_id,
        ]
    )
    tags = None
    volumes = response['Volumes']
    for volume in volumes:
        if volume.get('Tags'):
            tags = volume.get('Tags')

    return tags


# this function accepts the region and id of a particular network interface
# returns tags attached to that network interface if any else returns None
def describe_nwinterface_tags(region_name, network_interface_id):
    client = boto3.client('ec2', region_name=region_name)
    response = client.describe_network_interfaces(
        NetworkInterfaceIds=[
            network_interface_id,
        ],
    )
    tags = None
    network_interfaces = response['NetworkInterfaces']
    for interface in network_interfaces:
        if interface.get('TagSet'):
            tags = interface.get('TagSet')

    return tags


# this function accepts the tags of any resource
# returns the required tag values if present else return None
def validate_tags(tags):
    # the tags which are required
    true_tags = ['Name', 'Business_Vertical', 'Environment']
    tag_list = []

    for tag in tags:
        tag_list.append(tag['Key'])

    flag = 0

    for tag in true_tags:
        if tag in tag_list:
            flag += 1

    response = [
        {
            'Key': 'Name',
            'Value': None
        },
        {
            'Key': 'Business_Vertical',
            'Value': None
        },
        {
            'Key': 'Environment',
            'Value': None
        }
    ]

    if flag == 3:
        for tag in tags:
            if tag['Key'] == 'Name':
                value = tag['Value']
                response[0]['Value'] = value
            elif tag['Key'] == 'Business_Vertical':
                value = tag['Value']
                response[1]['Value'] = value
            elif tag['Key'] == 'Environment':
                value = tag['Value']
                response[2]['Value'] = value

        return response

    else:
        return None


def tag_volume(region_name, volume_id, tags):
    ec2 = boto3.resource('ec2', region_name=region_name)
    volume = ec2.Volume(volume_id)

    tag = volume.create_tags(
        Tags=tags
    )

    return tag


def tag_network_interface(region_name, interface_id, tags):
    ec2 = boto3.resource('ec2', region_name=region_name)
    network_interface = ec2.NetworkInterface(interface_id)

    tag = network_interface.create_tags(
        Tags=tags
    )

    return tag


# this function accepts region name and
# tags all the untagged resources
def tag_untagged_resource(region_name):
    print("{}, tagging untagged Ebs & Network interfaces".format(region_name))
    client = boto3.client('ec2', region_name=region_name)
    response = client.describe_instances().get('Reservations')
    tagged_volumes = {}
    tagged_eni = {}
    for instance in response:
        for inst in instance['Instances']:
            if inst.get('Tags'):
                tags = inst['Tags']
                # proceed only if the instance contains the required tags
                if validate_tags(tags):
                    required_tags = validate_tags(tags)

                    if inst.get('BlockDeviceMappings'):
                        for volumes in inst.get('BlockDeviceMappings'):
                            ebs = volumes['Ebs']
                            volume_id = ebs['VolumeId']
                            volume_tags = describe_volume_tags(region_name, volume_id)
                            flag = 0
                            if volume_tags:
                                if validate_tags(volume_tags):
                                    flag = 1
                                    print("skipping: {}".format(volume_id))
                            if flag == 0:
                                if volume_tags:
                                    for tag in required_tags:
                                        if tag not in volume_tags:
                                            volume_tags.append(tag)
                                else:
                                    volume_tags = required_tags
                                try:
                                    print("tagging: {}".format(volume_id))
                                    tag_volume(region_name, volume_id, volume_tags)
                                    tagged_volumes[volume_id] = volume_tags
                                except:
                                    tagged_volumes[volume_id] = "Error while tagging, Tags: {}".format(volume_tags)

                    if inst.get('NetworkInterfaces'):
                        for network in inst['NetworkInterfaces']:
                            network_interface_id = network['NetworkInterfaceId']
                            network_interface_tags = describe_nwinterface_tags(region_name, network_interface_id)
                            flag = 0
                            if network_interface_tags:
                                if validate_tags(network_interface_tags):
                                    flag = 1
                                    print("skipping: {}".format(network_interface_id))
                            if flag == 0:
                                if network_interface_tags:
                                    for tag in required_tags:
                                        if tag not in network_interface_tags:
                                            network_interface_tags.append(tag)
                                else:
                                    network_interface_tags = required_tags
                                try:
                                    print("tagging: {}".format(network_interface_id))
                                    tag_network_interface(region_name, network_interface_id, network_interface_tags)
                                    tagged_eni[network_interface_id] = network_interface_tags
                                except:
                                    tagged_eni[network_interface_id] = "Error while tagging, Tags: {}".format(
                                        network_interface_tags)

    print("\n-------------------------------------\n")
    if len(tagged_volumes) > 0:
        print("Following volumes were tagged with their respective tags:\n")
        print(tagged_volumes)
    else:
        print("No volumes tagged in {}".format(region_name))

    print("\n-------------------------------------\n")

    if len(tagged_eni) > 0:
        print("Following network interfaces were tagged with their respective tags:\n")
        print(tagged_eni)
    else:
        print("No network interfaces tagged in {}".format(region_name))
    print("\n-------------------------------------\n")


start = time.time()

# define the regions
regions = ['ap-south-1']
for region in regions:
    tag_untagged_resource(region)

end = time.time()

print("time taken = {} sec".format(end - start))
