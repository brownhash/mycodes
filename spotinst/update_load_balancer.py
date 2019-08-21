import requests
import json
import sys
from get_group_id import get_group_id


def update_load_balancer(account_id, token, group_name, lb_type, param):

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }

    group_id = get_group_id(group_name, account_id, token)

    if not group_id:
        print("No Elasticgroup found - ", group_name)
        sys.exit()
    else:
        print("Group_id: ", group_id)

    url = "https://api.spotinst.io/aws/ec2/group/{}?" \
          "accountId={}&autoApplyTags=true" \
        .format(group_id, account_id)

    if lb_type == 'target_group':
        tg_name = param[0]
        arn = param[1]

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
    elif lb_type == 'classic':
        clb_name = param[0]
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
    else:
        print("Not a recognised load-balancer type - ", type)
        sys.exit()

    req = requests.put(url, headers=header, data=json.dumps(body))
    print("Response - \n")
    print(req.text)
