import requests


def get_group_id(group_name, account_id, token):

    # param
    group_id = ""

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }

    url = 'https://api.spotinst.io/aws/ec2/group?accountId={}'\
        .format(account_id)

    # Getting all elastic group
    all_groups = requests.get(url, headers=header).json()["response"]["items"]

    for i in all_groups:
        g_id = i.get('id')
        name = i.get('name')
        if str(name) == str(group_name):
            group_id = g_id

    return group_id
