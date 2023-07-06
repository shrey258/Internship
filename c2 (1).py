import socket
 
IP = 'localhost'
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 8192
 
def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    """ Connecting to the server. """
    client.connect(ADDR)
 
    """ Opening and reading the file data. """
   # file = open("myfile.txt", "r")
    #data = file.read()
    data=b"O"*10*1024*1024
 
    """ Sending the filename to the server. """
    #client.send("myfile.txt".encode(FORMAT))
    #msg = client.recv(SIZE).decode(FORMAT)
    #print(f"[SERVER]: {msg}")
 
    """ Sending the file data to the server. """
    for i in range(6):
        client.sendall(data)
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
 
    """ Closing the file. """
    #file.close()
 
    """ Closing the connection from the server. """
    client.close()
 
 
if __name__ == "__main__":
    main()