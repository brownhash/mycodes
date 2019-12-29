import requests
import json
import sys

group_name = sys.argv[1]
type = sys.argv[2]

# params
clb_name = ""
tg_name = ""
arn = ""
group_id = ""

# credentials
token = ""
account_id = ""

header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(token)
}

url = 'https://api.spotinst.io/aws/ec2/group?accountId={}'.format(account_id)

# Getting all elastic group
allGroups = requests.get(url, headers=header).json()["response"]["items"]

for i in allGroups:
    id = i.get('id')
    name = i.get('name')
    if str(name) == str(group_name):
        group_id = id

if not group_id:
    print("No Elasticgroup found - ", group_name)
    sys.exit()

url = "https://api.spotinst.io/aws/ec2/group/{}?" \
      "accountId={}&autoApplyTags=true" \
    .format(group_id, account_id)

if type == 'target_group':
    tg_name = sys.argv[3]
    arn = sys.argv[4]

    body = {
        "group": {
            "compute": {
                "launchSpecification": {
                    "loadBalancersConfig": {
                        "loadBalancers": [
                            {
                                "name": tg_name,
                                "arn": arn,
                                "type": "TARGET_GROUP"
                            }
                        ]
                    }
                }
            }
        }
    }
elif type == 'classic':
    clb_name = sys.argv[3]
    body = {
        "group": {
            "compute": {
                "launchSpecification": {
                    "loadBalancersConfig": {
                        "loadBalancers": [
                            {
                                "name": clb_name,
                                "type": "CLASSIC"
                            }
                        ]
                    }
                }
            }
        }
    }

req = requests.put(url, headers=header, data=json.dumps(body))
print(req.text)
