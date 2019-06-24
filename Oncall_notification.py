default_webhook="[webhook-link]"

import time
import requests
import pymsteams
import sys




# retrieve details
# ------------------------------------------------------------
resp = requests.get('[host-name]/api/v0/teams')
if resp.status_code != 200:
    print("Error: {}", resp.status_code)

teams = resp.json()

# Fetch all links
# ------------------------------------------------------------
links = []
def link_fetch():
    for i in range(0, len(teams)):
        suffix = teams[i]
        ur = "[host-name]/team/"
        a = ur + suffix
        links.append(a)

link_fetch()
# ------------------------------------------------------------


# Fetch all summary(s)
# ------------------------------------------------------------
summary = []
def summary_fetch():
    for i in range(0, len(teams)):
        suffix = teams[i]
        prefix = "[host-name]/api/v0/teams/"
        suffix2 = "/summary"
        a = prefix + suffix + suffix2
        summary.append(a)

summary_fetch()
# ------------------------------------------------------------


# Fetch all webhooks
# ------------------------------------------------------------
webhook = []
def webhook_fetch():
    for i in range(0, len(teams)):
        a = "[host-name]/api/v0/teams/"
        suffix = teams[i]
        b = a + suffix
        resp = requests.get(b)
        data = resp.json()
        data2 = str(data)
        init = 0
        end = 0
        for i in range(0, len(data2)):
            if (data2[i] == "#"):
                init = i
                break
        init += 1
        for i in range(init + 1, len(data2)):
            if (data2[i] == "#" or data2[i] == "\""):
                end = i
                break

        webhook1 = data2[init:end]
        if ("#" not in data2):
            webhook1 = False

        webhook.append(webhook1)

webhook_fetch()
# ------------------------------------------------------------


# send message
# ------------------------------------------------------------
def send(webhookurl, link, messagestring):
    if (webhookurl != False and len(str(webhookurl)) > 50 and messagestring != "NULL"):
        # webhook url
        myTeamsMessage = pymsteams.connectorcard(webhookurl)
        myTeamsMessage.title("Oncall person")
        myTeamsMessage.text(messagestring)
        myTeamsMessage.addLinkButton("View OnCall", link)
        # send the message.
        status = myTeamsMessage.send()
        print("Link : {}".format(link))
        print("wbhookurl : {}".format(webhookurl))
        print("Status : {}".format(status))


# ------------------------------------------------------------


# print details
# ------------------------------------------------------------
def prints(webhookurl, link, messagestring):
    if (webhookurl != False and len(str(webhookurl)) > 50 and messagestring != "NULL"):
        print("Message: {}".format(messagestring))
        print("link: {}".format(link))
        print("Webhook: {}".format(webhookurl))
        print("\n")


# ------------------------------------------------------------


# retrieve messages
# ------------------------------------------------------------
def getmessage():
    messages = []
    daily_messages_flags_list = []
    for i in range(0, len(teams)):
        newdata = requests.get(summary[i])
        newdata2 = newdata.json()
        flag = 0
        flag1 = 0
        flag2 = 0
        flag_send_daily_message= 0
        if (newdata2):
            flag = 0
        else:
            flag = 1
            messagestring = "Null"

        if (flag == 0):
            if (newdata2.get('current').get('primary')):
                # current on-call
                full_name = newdata2.get('current').get('primary')[0].get('full_name')
                email = newdata2.get('current').get('primary')[0].get('user_contacts').get('email')
                call = newdata2.get('current').get('primary')[0].get('user_contacts').get('call')
                sms = newdata2.get('current').get('primary')[0].get('user_contacts').get('sms')
                starttime = newdata2.get('current').get('primary')[0].get('start')
                endtime = newdata2.get('current').get('primary')[0].get('end')
                start = time.strftime('%H:%M', time.localtime(starttime))
                end = time.strftime('%H:%M', time.localtime(endtime))
                flag1 = 1

                h = int(start[0:2]) + 5
                m = int(start[3:5]) + 30
                if (m >= 60):
                    h += 1
                    m = m - 60
                if (h >= 24):
                    h = h - 24

                if (len(str(h)) == 1 or len(str(m)) == 1):
                    if (len(str(h)) == 1):
                        h = "0" + str(h)
                    if (len(str(m)) == 1):
                        m = "0" + str(m)

                start = str(h) + ":" + str(m)

                h = int(end[0:2]) + 5
                m = int(end[3:5]) + 30
                if (m >= 60):
                    h += 1
                    m = m - 60
                if (h >= 24):
                    h = h - 24

                if (len(str(h)) == 1 or len(str(m)) == 1):
                    if (len(str(h)) == 1):
                        h = "0" + str(h)
                    if (len(str(m)) == 1):
                        m = "0" + str(m)

                end = str(h) + ":" + str(m)
                # Get period here
                # If the period is greater than a day 
                # Then send message every day at 9 AM.
                if starttime > endtime: # Well, this should never happen
                    print('Start time was before end time for user email' + str(email))
                else:
                    oncall_period = endtime - starttime
                    oncall_period_days = oncall_period / 86400 # seconds in a day
                    if oncall_period_days >= 2: 
                        print("oncall period is " + str(oncall_period_days) + " for " + str(email))
                        # Get current time in IST 
                        current_time_var = time.time() #epoch time
                        current_hour_var = time.strftime('%H', time.localtime(current_time_var))
                        print(current_hour_var)
                        if int(current_hour_var) == 3:
                            flag_send_daily_message = 1
                            print("set add today in message string")

            if (newdata2.get('next')) and (newdata2.get('next').get('primary')):
                # next on-call
                full_name2 = newdata2.get('next').get('primary')[0].get('full_name')
                email2 = newdata2.get('next').get('primary')[0].get('user_contacts').get('email')
                call2 = newdata2.get('next').get('primary')[0].get('user_contacts').get('call')
                sms2 = newdata2.get('next').get('primary')[0].get('user_contacts').get('sms')
                starttime2 = newdata2.get('next').get('primary')[0].get('start')
                endtime2 = newdata2.get('next').get('primary')[0].get('end')
                start2 = time.strftime('%H:%M', time.localtime(starttime2))
                end2 = time.strftime('%H:%M', time.localtime(endtime2))
                dates = time.strftime('%D', time.localtime(starttime2))
                flag2 = 1

                h = int(start2[0:2]) + 5
                m = int(start2[3:5]) + 30
                if (m >= 60):
                    h += 1
                    m = m - 60
                if (h >= 24):
                    h = h - 24

                if (len(str(h)) == 1 or len(str(m)) == 1):
                    if (len(str(h)) == 1):
                        h = "0" + str(h)
                    if (len(str(m)) == 1):
                        m = "0" + str(m)

                start2 = str(h) + ":" + str(m)

                h = int(end2[0:2]) + 5
                m = int(end2[3:5]) + 30
                if (m >= 60):
                    h += 1
                    m = m - 60
                if (h >= 24):
                    h = h - 24

                if (len(str(h)) == 1 or len(str(m)) == 1):
                    if (len(str(h)) == 1):
                        h = "0" + str(h)
                    if (len(str(m)) == 1):
                        m = "0" + str(m)

                end2 = str(h) + ":" + str(m)
        print(email)
        for j in range(0, len(email)):
            if (email[j] == "@"):
                break
        teams_user = email[0:j]

        for k in range(0, len(email2)):
            if (email2[k] == "@"):
                break
        teams_user2 = email2[0:k]

        if (len(str(newdata2)) < 50):
            messagestring = "No OnCall Data Found"

        elif (flag == 0):
            if (flag1 == 1 and flag2 == 1):
                messagestring = "Today " + full_name.upper() + " is oncall for " + teams[
                    i] + ", from " + start + " to " + end + ". Email- " + email + " , Teams Username- " + teams_user + ". And " + full_name2.upper() + " is next oncall for " + \
                                teams[
                                    i] + ", from " + start2 + " to " + end2 + " on (MM/DD/YY) " + dates + ". Email- " + email2 + " , Teams Username- " + teams_user2
            elif (flag1 == 0 and flag2 == 1):
                messagestring = full_name2.upper() + " is next oncall for " + teams[
                    i] + ", from " + start2 + " to " + end2 + " on (MM/DD/YY)" + dates + ". Email- " + email2 + " , Teams Username- " + teams_user
            elif (flag1 == 1 and flag2 == 0):
                messagestring = "Today " + full_name.upper() + " is oncall for " + teams[
                    i] + ", from " + start + " to " + end + ". Email- " + email + " , Teams Username- " + teams_user

        if (flag == 0):
            if (teams[i] == "PRIME" or teams[i] == "PTS" or teams[i] == "ZTS" or teams[i] == "OTS" or teams[
                i] == "FTS"):
                if (flag1 == 1 and flag2 == 1):
                    messagestring = "Today " + full_name.upper() + " is oncall for " + teams[
                        i] + ", from " + start + " to " + end + ". Email- " + email + ". And " + full_name2.upper() + " is next oncall for " + \
                                    teams[
                                        i] + ", from " + start2 + " to " + end2 + " on (MM/DD/YY)" + dates + ". Email- " + email2
                elif (flag1 == 0 and flag2 == 1):
                    messagestring = full_name2.upper() + " is next oncall for " + teams[
                        i] + ", from " + start2 + " to " + end2 + " on (MM/DD/YY)" + dates + ". Email- " + email2
                elif (flag1 == 1 and flag2 == 0):
                    messagestring = "Today " + full_name.upper() + " is oncall for " + teams[
                        i] + ", from " + start + " to " + end + ". Email- " + email

        messages.append(messagestring)
        daily_messages_flags_list.append(flag_send_daily_message)

    return (messages, daily_messages_flags_list)


# ------------------------------------------------------------

msg, daily_messages_flags_list = getmessage()

# send test messages once when the script is run
# ------------------------------------------------------------
#for x in range(0, len(teams)):
#    send(webhook[x], links[x], msg[x])
# ------------------------------------------------------------


# hourly executing loop to send notification if any change occur5
# ------------------------------------------------------------
while (1 > 0):
    time.sleep(3600)
    teams=resp.json()
    webhook_fetch()
    link_fetch()
    summary_fetch()
    msgnew, daily_messages_flags_list = getmessage()
    for y in range(0, len(teams)):
        print(teams[y])
        print("Daily message flag : {}".format(daily_messages_flags_list[y]))
        if (msg[y] != msgnew[y]) or daily_messages_flags_list[y] == 1:
            send(webhook[y], links[y], msgnew[y])
    sys.stdout.flush()
    msg, daily_messages_flags_list_old = getmessage()
# -----------------------------------------------------------
