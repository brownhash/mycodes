import sys
from update_load_balancer import update_load_balancer
from pause_resume_inst import pause_resume_inst

group_name = sys.argv[1]
account_id = sys.argv[2]
token = sys.argv[3]
action = sys.argv[4]
params = sys.argv[5].split(" ")


if action == "add load balancer":
    lb_type = params[0]
    param = []
    for i in range(1, len(params)):
        param.append(params[i])

    update_load_balancer(account_id, token, group_name, lb_type, param)

elif action == "pause or resume elastic group":
    act = params[0]
    pause_resume_inst(account_id, token, group_name, act)
