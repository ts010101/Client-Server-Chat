import socket

#Step 1: The server creates a socket and binds to ‘localhost’ and port xxxx
HOST, PORT = "localhost", 3351
s_sock = socket.socket()
s_sock.bind((HOST, PORT))
print("Server listening on: {} on port: {}".format(HOST,PORT))

#Step 2: The server then listens for a connection
s_sock.listen(2)
conn, address = s_sock.accept()
print("Connection by: {}".format(address))
print("Waiting for message...")

#Step 3: When connected, the server calls recv to receive data
msg = conn.recv(1024).decode()

# Step 4: The server prints the data, then prompts for a reply
print(str(msg))
print("Type /q to quit")
print("Enter message to send")
while True:
    msg = input(">")
    #Step 5: If the reply is /q, the server quits
    if msg == "/q": break

    #Step 6: Otherwise, the server sends the reply
    conn.send(msg.encode())

    #Step 7: Back to step 3
    msg = conn.recv(1024).decode()
    if not msg: break

    print(str(msg))

#Step 8: Sockets are closed
conn.close()


