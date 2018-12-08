import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Hey! You are on | {} | with IP Address | {} |".format(hostname,IPAddr))
