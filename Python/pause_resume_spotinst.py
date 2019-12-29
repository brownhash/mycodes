# pausing and resuming spot instances based on their group tags

import requests
import sys


# Parameters
tag_key = "spot_pause"
tag_value = "yes"
account_id = str(sys.argv[1])
token = str(sys.argv[2])
action = str(sys.argv[3])


def list_stateful_instances(group_id, account_id, bearer_token):

    ur = "https://api.spotinst.io/aws/ec2/group/{}/" \
         "statefulInstance?accountId={}".format(group_id, account_id)
    header = {'Authorization': 'Bearer ' + bearer_token}
    instances = requests.get(ur, headers=header).json()
    items = instances.get('response').get('items')

    stateful_instance_id = []

    for inst in items:
        ssi = inst.get('id')
        stateful_instance_id.append(ssi)

    return(stateful_instance_id)


def action_on_stateful(group_id, stateful_inst_id, action, account_id, token):

    url = "https://api.spotinst.io/aws/ec2/group/{}/" \
          "statefulInstance/{}/{}?accountId={}"\
        .format(group_id, stateful_inst_id, action, account_id)
    header = {'Authorization': 'Bearer ' + token}
    requests.put(url, headers=header)


# Getting all elastic groups
headers = {'Authorization': 'Bearer ' + token}
url = 'https://api.spotinst.io/aws/ec2/group?accountId={}'.format(account_id)

# Getting all elastic group
allGroups = requests.get(url, headers=headers).json()["response"]["items"]
count = 0

paused_groups = []
resumed_groups = []

for i in allGroups:
    group_id = i.get('id')
    tags = i.get('compute').get('launchSpecification').get('tags')

    for k in tags:
        if k.get('tagKey') == tag_key and k.get('tagValue') == tag_value:
            stateful_instance_ids = \
                list_stateful_instances(group_id, account_id, token)
            if len(stateful_instance_ids) > 0:
                for si in stateful_instance_ids:
                    action_on_stateful(group_id, si, action, account_id, token)
                    if action == "pause":
                        paused_groups.append(group_id)
                    elif action == "resume":
                        resumed_groups.append(group_id)

if len(paused_groups) > 0 or len(resumed_groups) > 0:
    if action == "pause":
        print("--------------------------------------------\n")
        print("Paused instances (Stating all group ids)\n")
        print(str(paused_groups) + "\n")
        print("--------------------------------------------\n")

    elif action == "resume":
        print("--------------------------------------------\n")
        print("Resumed instances (Stating all group ids)\n")
        print(str(resumed_groups) + "\n")
        print("--------------------------------------------\n")


"""
import time
to store logs

if(len(paused_groups) > 0):
    writer = open('paused_spotinst_logs.txt', 'a')
    timestamp = time.strftime("%d/%m/%y - %H:%M:%S")
    writer.write("-----------------------------\n")
    writer.write(str(timestamp)+"\n")
    writer.write("-----------------------------\n")
    writer.write("Paused instance group ids -\n")
    writer.write(str(paused_groups) + "\n")
    writer.close()
else:
    writer = open('paused_spotinst_logs.txt', 'a')
    timestamp = time.strftime("%d/%m/%y - %H:%M:%S")
    writer.write("-----------------------------\n")
    writer.write(str(timestamp)+"\n")
    writer.write("-----------------------------\n")
    writer.write("No instances were paused\n")
    writer.close()

"""
