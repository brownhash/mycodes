import re


def email_check(email, domain):
    response = re.findall("^[a-z]+[1-9]*[a-z]*@{}$".format(domain), email)
    if response:
        return "Valid"
    else:
        return "Invalid"


print(email_check("harrydbst123@gmail.com", "gmail.com"))