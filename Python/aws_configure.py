import sys


def get_help():
    print("Error: No options found")
    print("Usage:\n\tpython aws_configure.py [option]\n"
          "\tPossible options: -h, -option1, -option2\n")


config = {
    "acc1": {
        "access": "string",
        "secret_access": "string"
    },
    "acc2": {
        "access": "string",
        "secret_access": "string"
    },
}


def create_config(access_key, secret_access_key):

    filepath = "/Users/harshit.sharma/.aws/credentials"
    format = "[default]\naws_access_key_id = {}\naws_secret_access_key = {}"\
        .format(access_key, secret_access_key)

    writer = open(filepath, 'w')
    writer.write(format)
    writer.close()


try:
    option = sys.argv[1]
    if option == "-option1":
        access_key = config.get('acc1').get('access')
        secret_access_key = config.get('acc1').get('secret_access')

        create_config(access_key, secret_access_key)

        print("AWS Config successful for Account 1")

    elif option == "-option2":
        access_key = config.get('acc2').get('access')
        secret_access_key = config.get('acc2').get('secret_access')

        create_config(access_key, secret_access_key)

        print("AWS Config successful for Account 2")

    elif option == "-h":
        get_help()

    else:
        get_help()

except:
    get_help()
