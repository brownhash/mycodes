import requests


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

    return stateful_instance_id
