import socket
 
def Main():
        host = 'localhost'
        port = 9999
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input(" -> ")

        print ("closing connection")           
        mySocket.close()
 
if __name__ == '__main__':
    Main()