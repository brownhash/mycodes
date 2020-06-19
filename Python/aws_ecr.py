import boto3
registry_id = 'String'


def get_repos(client):
    try:
        repos = []
        response = client.describe_repositories()
        for repo in response.get('repositories'):
            repos.append(repo)

        return repos
    except:
        return None


def get_policy(client, reg_id, repo):
    try:
        response = client.get_lifecycle_policy(
            registryId=reg_id,
            repositoryName=str(repo)
        )
        return response.get('lifecyclePolicyText')
    except:
        return None


def put_policy(client, reg_id, repo, policy):
    try:
        response = client.put_lifecycle_policy(
            registryId=reg_id,
            repositoryName=str(repo),
            lifecyclePolicyText=str(policy)
        )
        return response
    except:
        return None


def get_images(client, reg_id, repo):
    try:
        response = client.describe_images(
            registryId=reg_id,
            repositoryName=repo,
            filter={
                'tagStatus': 'ANY'
            }
        )
        return response.get('imageDetails')
    except:
        return None


client_mum = boto3.client('ecr', region_name='ap-south-1')

"""
example rule format for put policy -

(1)
rule_since_any = '{"rules":' \
                 '[{"rulePriority": 1,' \
                 '"description": "deletion of images older than 5 days",' \
                 '"selection":' \
                 '{"tagStatus": "any",' \
                 '"countType": "sinceImagePushed",' \
                 '"countUnit": "days",' \
                 '"countNumber": 5},' \
                 '"action":' \
                 '{"type": "expire"}}]}'

(2)
rule_since_tagged = '{"rules":' \
                    '[{"rulePriority":1,' \
                    '"description":"deletion of images older than 5 days",' \
                    '"selection":' \
                    '{"tagStatus":"tagged",' \
                    '"tagPrefixList":["prod","policy_on"],' \
                    '"countType":"sinceImagePushed",' \
                    '"countUnit":"days",' \
                    '"countNumber":5},' \
                    '"action":' \
                    '{"type":"expire"}}]}'
(3)
rule_count_any = '{"rules":' \
                 '[{"rulePriority": 1,' \
                 '"description": "deletion of images when number greater than 10",' \
                 '"selection":' \
                 '{"tagStatus": "any",' \
                 '"countType": "imageCountMoreThan",' \
                 '"countNumber": 10},' \
                 '"action":' \
                 '{"type": "expire"}}]}'

(4)                    
rule_count_tagged = '{"rules":' \
                    '[{"rulePriority":1,' \
                    '"description":"deletion of images when number greater than 10",' \
                    '"selection":' \
                    '{"tagStatus":"tagged",' \
                    '"tagPrefixList":["prod","policy_on"],' \
                    '"countType":"imageCountMoreThan",' \
                    '"countNumber":10},' \
                    '"action":' \
                    '{"type":"expire"}}]}'
"""

