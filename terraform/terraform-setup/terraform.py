import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
VERSION = None
FILENAME = "terraform"

# this path is for macOS
# change it for ubuntu / centos
BIN_PATH = "/usr/local/bin/"

if len(sys.argv) == 2:
    VERSION = str(sys.argv[1])
elif len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Syntax error")

if VERSION == "11" or VERSION == "12":
    PATH = PATH + "/" + VERSION
    COMMAND = "cp {}/{} {}".format(PATH, FILENAME, BIN_PATH)
    try:
        os.system(COMMAND)
        os.system("terraform --version")
    except Exception as error:
        print("Error!\n{}".format(error))
else:
    print("\nHELP:\n"
          "Usage - python3 terraform.py [option]\n"
          "Options - 11 / 12 / help\n"
          "For available terraform versions, visit:\n"
          "https://releases.hashicorp.com/terraform/")

# in .bashrc file set the path to directory
# copy the bash rc to root
# run, $ source ~/.bashrc

# now use 2 or more versions of terraform on the go
# run, $ terraform11 for terraform v0.11.14
# run, $ terraform12 for terraform v0.12.16
