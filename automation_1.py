import os

password=str(input("Enter the system password:"))

def install_dependency(password):
    command = "echo " + str(password) + " | sudo -S apt-get install ansible"
    command2 = "echo " + str(password) + " | sudo -S apt-get install git"
    print("Installing dependencies -")
    try:
        os.system(command)
        print("Ansible: done")
    except:
        print("Some error occured while installing Ansible")
    try:
        os.system(command2)
        print("Git: done")
    except:
        print("Some error occured while installing Nginx")

def pull_repo(password):
    command = "echo " + str(password) + " | sudo -S git clone <repo-address>"
    try:
        os.system(command)
        print("Repository: done")
    except:
        print("Some error occured while cloning the repository")

def run_ansible():
    command = "ansible-playbook /dir-name/playbook.yml"
    try:
        os.system(command)
        print("Nginx: done")
    except:
        print("Some error occured while running ansinle-playbook")

def get_html(password):
    command = "echo " + str(password) + " | sudo -S git clone <repo-address>"
    try:
        os.system(command)
        print("HTML-Repository: done")
    except:
        print("Some error occured while cloning the HTML-repository")

def copy_config(password):
    command = "echo " + str(password) + " | sudo -S cp /home/username/congig/default /etc/nginx/sites-available/default"
    try:
        os.system(command)
        print("Nginx-Configuration: done")
    except:
        print("Some error occured while configuring nginx")

install_dependency(password)
pull_repo(password)
run_ansible()
get_html(password)
copy_config(password)
