#pre-requisite
#pip install pymsteams

import requests
import pymsteams

resp = requests.get('oncall rest api url')
if resp.status_code != 200:
    print("Error: {}",resp.status_code)
oncall=resp.json()

#current on-call
full_name=oncall.get('current').get('primary')[0].get('full_name')
email=oncall.get('current').get('primary')[0].get('user_contacts').get('email')
call=oncall.get('current').get('primary')[0].get('user_contacts').get('call')

#secondary on-call
full_name2=oncall.get('next').get('primary')[0].get('full_name')
email2=oncall.get('next').get('primary')[0].get('user_contacts').get('email')
call2=oncall.get('next').get('primary')[0].get('user_contacts').get('call')

team=oncall.get('current').get('primary')[0].get('team')

for i in range(0,len(email)):
    if (email[i]=="@"):
        break

teams_user=email[0:i]

for i in range(0,len(email2)):
    if (email2[i]=="@"):
        break

teams_user2=email2[0:i]

messagestring="Today "+full_name.upper()+" is oncall for "+team+". Teams Username- "+teams_user+" , Phone No- "+call+" , Email- "+email+". And "+full_name2.upper()+" is secondary oncall for "+team+". Teams Username- "+teams_user2+" , Phone No- "+call2+" , Email- "+email2

# webhook url
myTeamsMessage = pymsteams.connectorcard("MS - Teams Webhook URL")

myTeamsMessage.title("Oncall person")
myTeamsMessage.text(messagestring)
myTeamsMessage.addLinkButton("View OnCall", "Oncall dashboard url")
# send the message.
myTeamsMessage.send()
