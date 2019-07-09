import boto3

def get_spotInstances(region_name):
    ec2 = boto3.client('ec2', region_name=region_name)

    spot_instances = ec2.describe_spot_instance_requests()
    instances = spot_instances.get('SpotInstanceRequests')

    spot_list=[]
    instance_types=[]
    instance_count=[]
    result={}
    for i in instances:
        if(i.get('State')=='active'):
            type=i.get('LaunchSpecification').get('InstanceType')
            spot_list.append(type)

    for i in spot_list:
        if(i not in instance_types):
            instance_types.append(i)

    for i in instance_types:
        count=spot_list.count(i)
        instance_count.append(count)

    for i in range(0,len(instance_types)):
        key=instance_types[i]
        val=instance_count[i]
        result[key]=val

    return(result)
