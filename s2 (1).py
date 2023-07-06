import socket
import time 
IP = 'localhost'
PORT = 4455
ADDR = (IP, PORT)
SIZE = 8192
FORMAT = "utf-8"
 
def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)
 
    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")
 
    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
 
        """ Receiving the filename from the client. """
        #filename = conn.recv(SIZE).decode(FORMAT)
        #print(f"[RECV] Receiving the filename.")
        # file = open(filename, "w")
        #conn.send("Filename received.".encode(FORMAT))
        speed = 0
        """ Receiving the file data from the client. """
        for i in range(6):
            start_time=time.time()
            data = conn.recv(SIZE)#.decode(FORMAT)
            print(f"[RECV] Receiving the file data.")
            #file.write(data)
            end_time=time.time()
            speed += 8*10/(end_time-start_time)
            conn.send("File data received".encode(FORMAT))
            print('The speed is '+str(speed)+'Mbps')
        avg = speed/5
        conn.send(str('The speed is '+str(avg)+'Mbps').encode(FORMAT))
 
        """ Closing the file. """
        #file.close()
 
        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
 
if __name__ == "__main__":
    main()