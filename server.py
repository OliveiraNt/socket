import socket
 
def Main():
    host = "localhost"
    port = 9999
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            if "+" in str(data):
                a = str(data).split("+")
                data = str(int(a[0]) + int(a[1]))

            elif "-" in str(data):
                a = str(data).split("-")
                data = str(int(a[0]) - int(a[1]))

            elif "*" in str(data):
                a = str(data).split("*")
                data = str(int(a[0]) * int(a[1]))

            elif "/" in str(data):
                a = str(data).split("/")
                data = str(int(a[0]) / int(a[1]))

            else:
                data = "Operation is not supported"

            print ("sending: " + str(data))
            conn.send(data.encode())

    print ("Terminating connection with: " + str(addr))         
    conn.close()
     
if __name__ == '__main__':
    Main()