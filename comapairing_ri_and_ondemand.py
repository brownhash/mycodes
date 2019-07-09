from aws_instances_per_instance_type import getInstances
from aws_reserved_instnces_per_instance_type import get_reservedInstances
from aws_spot_instances_per_instance_type import get_spotInstances

regions=['ap-southeast-1','ap-south-1']

total_instances={}
total_spot={}
total_reserved={}
ondemand={}

for i in regions:
    instances=getInstances(i)
    for j in instances:
        if(total_instances.get(j)):
            val=total_instances.get(j)+instances.get(j)
            total_instances[j]=val
        else:
            total_instances[j]=instances.get(j)

    spot = get_spotInstances(i)
    for k in spot:
        if (total_spot.get(k)):
            val2 = total_spot.get(k) + spot.get(k)
            total_spot[k] = val2
        else:
            total_spot[k] = spot.get(k)

    reserved = get_reservedInstances(i)
    for x in reserved:
        if (total_reserved.get(x)):
            val3 = total_reserved.get(x) + reserved.get(x)
            total_reserved[x] = val3
        else:
            total_reserved[x] = reserved.get(x)


print("Reserved Instances")
print(total_reserved)
#print("\nNormal Ec2")
#print(total_instances)
#print("\nSpot Instances")
#print(total_spot)


for i in total_spot:
    if(not total_instances.get(i)):
        ondemand[i]=total_spot.get(i)

for i in total_instances:
    if(total_spot.get(i)):
        val=total_instances.get(i)-total_spot.get(i)
        ondemand[i]=val
    else:
        ondemand[i]=total_instances.get(i)

print("\nOndemand")
print(ondemand)
