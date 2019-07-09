#pre-requisite: Aws configure
import boto3

def getInstances(region_name):
    ec2 = boto3.resource('ec2', region_name=region_name)

    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)

    # instantiate empty array
    RunningInstances = []
    for instance in instances:
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.instance_type)

    instance_types = []
    instance_count = []

    for i in RunningInstances:
        if (i not in instance_types):
            instance_types.append(i)
    # print(instance_types)

    for i in instance_types:
        count = RunningInstances.count(i)
        instance_count.append(count)
    # print(instance_count)

    result = {}
    for i in range(0, len(instance_types)):
        result[instance_types[i]] = instance_count[i]

    return(result)
