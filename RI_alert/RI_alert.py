from get_instances_per_instance_type import getInstances
from get_reserved_instances_per_instance_type import get_reservedInstances
from get_spot_instances_per_instance_type import get_spotInstances
from instance_equivalence import instanceEquivalence
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

def alert(region):

    total_instances = {}
    total_spot = {}
    total_reserved = {}
    ondemand = {}
    alert = []

    instances = getInstances(region)
    for j in instances:
        if (total_instances.get(j)):
            val = total_instances.get(j) + instances.get(j)
            total_instances[j] = val
        else:
            total_instances[j] = instances.get(j)

    spot = get_spotInstances(region)
    for k in spot:
        if (total_spot.get(k)):
            val2 = total_spot.get(k) + spot.get(k)
            total_spot[k] = val2
        else:
            total_spot[k] = spot.get(k)

    reserved = get_reservedInstances(region)
    for x in reserved:
        if (total_reserved.get(x)):
            val3 = total_reserved.get(x) + reserved.get(x)
            total_reserved[x] = val3
        else:
            total_reserved[x] = reserved.get(x)

    for i in total_spot:
        if (not total_instances.get(i)):
            ondemand[i] = total_spot.get(i)

    for i in total_instances:
        if (total_spot.get(i)):
            val = total_instances.get(i) - total_spot.get(i)
            ondemand[i] = val
        else:
            ondemand[i] = total_instances.get(i)

    equated_ondemand = instanceEquivalence(ondemand)
    equated_reserved = instanceEquivalence(total_reserved)

    for i in equated_reserved:
        if (equated_reserved.get(i) > abs(equated_ondemand.get(i))):
            message="RI over provisioned for "+str(i)+" type in "+str(region)+" region. "
            status=str(i)+" in ondemand = "+str(abs(equated_ondemand.get(i)))+" and in RI = "+str(equated_reserved.get(i))
            alert.append(message+status)

    if args.v:
        equated_spot = instanceEquivalence(total_spot)
        equated_inst = instanceEquivalence(total_instances)
        fetch_log = {'ec2': equated_inst, 'spot_instances': equated_spot, 'reserved_instances':equated_reserved}
        debug_status = {'debug_log':fetch_log}
        alert.append(debug_status)

    return(alert)

print(alert('ap-south-1'))
print(alert('ap-southeast-1'))