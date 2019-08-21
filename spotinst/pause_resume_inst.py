import requests
import sys
from list_stateful_instances import list_stateful_instances
from get_group_id import get_group_id


def action_on_stateful(group_id, stateful_inst_id, action, account_id, token):

    url = "https://api.spotinst.io/aws/ec2/group/{}/" \
          "statefulInstance/{}/{}?accountId={}"\
        .format(group_id, stateful_inst_id, action, account_id)
    header = {'Authorization': 'Bearer ' + token}
    requests.put(url, headers=header)


def pause_resume_inst(account_id, token, group_name, action):
    group_id = get_group_id(group_name, account_id, token)

    if not group_id:
        print("No elasticgoup found - ", group_name)
        sys.exit()
    else:
        print("Group ID - ", group_id)

    instances_list = list_stateful_instances(group_id, account_id, token)

    if instances_list:
        for id in instances_list:
            action_on_stateful(group_id, id, action, account_id, token)
            print("{} - {}".format(action + "d", id))
    else:
        print("No instances found in the mentioned group")
        sys.exit()
