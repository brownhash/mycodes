import sys


def get_help():
    print("\nPlease add some options\n")


def create_config(access_key, secret_access_key):

    filepath = "/Users/harshit.sharma/.aws/credentials"
    format = "[default]\naws_access_key_id = {}\naws_secret_access_key = {}"\
        .format(access_key, secret_access_key)

    writer = open(filepath, 'w')
    writer.write(format)
    writer.close()


if not sys.argv[1]:
    get_help()
else:
    option = sys.argv[1]
    if option == "-r":
        access_key = ""
        secret_access_key = ""

        create_config(access_key, secret_access_key)

    elif option == "-p":
        access_key = ""
        secret_access_key = ""

        create_config(access_key, secret_access_key)

    else:
        get_help()