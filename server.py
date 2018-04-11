import socket

from _thread import *
import threading

def threaded(c, addr):
    while True:
 
        # data received from client
        data = c.recv(1024).decode()
        if not data:

                print("Terminating connection with: " + str(addr[0]) + ':' + str(addr[1]))
                break
        print ("from connected user " + str(addr[0]) + ':' + str(addr[1]) + " -> " + str(data))
             
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
        c.send(data.encode())
 
    # connection closed
    c.close()
 
def Main():
    host = "localhost"
    port = 9998
     
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind((host,port))
    print("socket binded to post", port)
     
    mySocket.listen(5)
    print("socket is listening")

    while True:

            conn, addr = mySocket.accept()

            print('Connected to :', addr[0], ':', addr[1])

            start_new_thread(threaded, (conn, addr,))

            

    print ("Closing socket")         
    mySocket.close()
     
if __name__ == '__main__':
    Main()
