import socket

#Step 1: The client creates a socket and connects to ‘localhost’ and port xxxx
HOST, PORT = "localhost", 3351
c_sock = socket.socket()
c_sock.connect((HOST, PORT))
print("Connected to: {} on port: {}".format(HOST,PORT))

#Step 2: When connected, the client prompts for a message to send
print("Type /q to quit")
print("Enter message to send")
msg = input(">")

#Step 3: If the message is /q, the client quits
while msg != "/q":
    #Step 4: Otherwise, the client sends the message
    c_sock.send(msg.encode())

    #Step 5: The client calls recv to receive data
    msg = c_sock.recv(1024).decode()

    #Step 6: The client prints the data
    print(str(msg))

    #Step 7: Back to step 2
    msg = input(">")

#Step 8: Sockets are closed
c_sock.close()


