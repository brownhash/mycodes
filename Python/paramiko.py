import paramiko
import sys


class paramiko_conn:

    def connection(self, method, host, user, auth_value):
        if str(method) == "-k" or str(method) == "--key":
            try:
                key = paramiko.RSAKey.from_private_key_file(str(auth_value))
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(hostname=host, username=user, pkey=key)

                return ssh_client

            except Exception as error:
                print("An error was encountered while connecting using key.\n{}\nAborting the process . . .").format(
                    error)
                sys.exit()

        elif str(method) == "-p" or str(method) == "--password":
            try:
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(hostname=host, username=user, password=auth_value)

                return ssh_client

            except Exception as error:
                print(
                    "An error was encountered while connecting using password.\n{}\nAborting the process . . .").format(
                    error)
                sys.exit()

        elif str(method) == "-h" or str(method) == "--help":
            print("Usage:\nparamiko_conn().connection([auth type] [hostname] [username] [auth value])\n"
                  "eg: paramiko_conn().connection(\"-k\" \"127.0.0.1\" \"root\" \"path_to_pem_file\")\n"
                  "eg: paramiko_conn().connection(\"-p\" \"127.0.0.1\" \"root\" \"password\")\n")
            sys.exit()

        else:
            print("Usage:\nparamiko_conn().connection([auth type] [hostname] [username] [auth value])\n"
                  "eg: paramiko_conn().connection(\"-k\" \"127.0.0.1\" \"root\" \"path_to_pem_file\")\n"
                  "eg: paramiko_conn().connection(\"-p\" \"127.0.0.1\" \"root\" \"password\")\n")
            sys.exit()

    def put_file(self, auth, local_filepath, dest_filepath):

        try:
            ftp_client = auth.open_sftp()
            ftp_client.put(str(local_filepath), str(dest_filepath))
            print("Success!")
            ftp_client.close()
        except Exception as error:
            print("An error was encountered while copying the file:\n{}").format(error)

    def execute_command(self, auth, command):

        try:
            stdin, stdout, stderr = auth.exec_command(str(command))
            print("Executed:")
            print("-----------------------")
            print(stdout.readlines())
            print("-----------------------")
        except Exception as error:
            print("An error was encountered while executing -> {}\n{}".format(str(command),error))

key_path = "/Users/harshit.sharma/.ssh/id_rsa/"
auth_token = paramiko_conn().connection("-p", "localhost", "harshit.sharma", "rivigo@123")
paramiko_conn().execute_command(auth_token, "ls")