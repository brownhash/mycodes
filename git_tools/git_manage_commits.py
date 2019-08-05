def print_dash(message):
    s = str(message)
    l = len(s)
    print("-" * l)

def print_error_dash(message):
    s = str(message)
    l = len(s)
    print("!" * l)

def print_head_dash():
    print("#" * 53)

def manage_commits():
    import os

    def git_run(filename, commit_message, branch):
        try:
            command = "git checkout -b" + branch
            try:
                os.system(command)
                message = "Git creating branch >>{}<<: Done".format(branch)
                print_dash(message)
                print(message)
                print_dash(message)
            except:
                message = "Already in >>{}<< branch".format(branch)
                print_dash(message)
                print(message)
                print_dash(message)
            command = "git checkout " + branch
            try:
                os.system(command)
                message = "Git checkout to >>{}<< branch: Done".format(branch)
                print_dash(message)
                print(message)
                print_dash(message)
            except:
                message = "Already in >>{}<< branch".format(branch)
                print_dash(message)
                print(message)
                print_dash(message)

            command = "git pull origin " + branch
            os.system(command)
            message = "Pulled the latest commit from specified branch"
            print_dash(message)
            print(message)
            print_dash(message)

            command = "git add " + filename
            os.system(command)
            message = "File >>{}<< added to current stack".format(filename)
            print_dash(message)
            print(message)
            print_dash(message)

            command = "git commit -am " + "\"" + commit_message + "\""
            os.system(command)
            message_format = ">>{}<< appended as commit message".format(commit_message)
            print_dash(message)
            print(message_format)
            print_dash(message)

            command = "git push origin " + branch
            os.system(command)
            message = "All changes pushed to >>{}<< branch".format(branch)
            print_dash(message)
            print(message_format)
            print_dash(message)

        except:
            message = "Some error occured"
            print_error_dash(message)
            print(message_format)
            print_error_dash(message)

    command = "git status"
    print_head_dash()
    print("----------------------------------------------------")
    print("Current changes in repository - ")
    print("----------------------------------------------------")
    os.system(command)
    print_head_dash()
    filename = str(input(
        "Enter filenames separated by spaces\nExample: >>> file1 file2 file3\nEnter file names >>>")).split(
        " ")
    branch = str(input("Enter branch >>>"))
    message_status = str(input("Use same commit message for all files(y or n)\n>>>"))
    if (message_status == "Y" or message_status == "y"):
        message = str(input("Enter commit message >>>"))
        for i in filename:
            try:
                file_check = open(i, "r")
                file_check.close()

                print_head_dash()
                print("Filename - \"{}\"".format(i))
                print_head_dash()
                git_run(i, message, branch)

            except:
                print_head_dash()
                print(">>{}<< no such file exists".format(i))
                print_head_dash()

        print_head_dash()
        print("FINISHED")
        print_head_dash()

    elif (message_status == "N" or message_status == "n"):
        for i in filename:
            try:
                file_check = open(i, "r")
                file_check.close()

                print_head_dash()
                print("Filename - \"{}\"".format(i))
                print_head_dash()
                message = str(input("Enter commit message for {} >>>".format(i)))
                git_run(i, message, branch)

            except:
                print_head_dash()
                print(">>{}<< no such file exists".format(i))
                print_head_dash()

        print_head_dash()
        print("FINISHED")
        print_head_dash()

manage_commits()