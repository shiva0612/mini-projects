import socket

s = socket.socket()
name = socket.gethostname()
IP = socket.gethostbyname(name)

print(f"server with IP {IP} is hosted ")

s.bind((IP,9999))
s.listen(3)

c,add = s.accept()
print("connected with : " + add[0] + "using port : " + str(add[1]))
for i in range(1,100):

    it = input("enter command : ")
    if it == "quit":
        c.close()
        s.close()
        sys.exit()
    else:
        c.send(it.encode())
        filename = input("enter filename: ")
        file = open(filename,'wb')
        while True:
            data = c.recv(1024)
            if not data:
                print("done sending:")
                break
            else:
                file.write(data)
                print("writing:")
        file.close()
        c.close()
        s.close()




