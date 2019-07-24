def git_config():
    import os

    def global_config(username, email):
        command = "git config --global user.name \"" + username + "\""
        os.system(command)
        command = "git config --global user.email \"" + email + "\""
        os.system(command)
        message = "Username: {}, Email: {} have been set globally".format(username, email)
        print("-" * len(message))
        print(message)
        print("-" * len(message))

    def local_config(username, email):
        command = "git config user.name \"" + username + "\""
        os.system(command)
        command = "git config user.email \"" + email + "\""
        os.system(command)
        message = "Username: {}, Email: {} have been set locally".format(username, email)
        print("-" * len(message))
        print(message)
        print("-" * len(message))

    print("(G) Global config\n(L) Local config i.e. config restricted to particular directory\n")
    option = str(input("What type of configuration do you need (G or L)"))
    username = str(input("Enter username >>>"))
    email = str(input("Enter email >>>"))
    if (option == "G" or option == "g"):
        global_config(username, email)
    elif (option == "L" or option == "l"):
        local_config(username, email)

git_config()