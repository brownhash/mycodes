import requests
import sys


def github_contrib(username):
    url = "https://www.github.com/"
    a = requests.get(url+str(username))

    data = str(a.text)

    splitter = "contributions\n        in the last year"

    listed = data.split(splitter)[0][::-1]
    contribution = listed.split(" ")[1][::-1]

    return contribution


if len(sys.argv) > 1:
    username = sys.argv[1]
    print(github_contrib(username))
else:
    username = str(input("Enter github username > "))
    print(github_contrib(username))
