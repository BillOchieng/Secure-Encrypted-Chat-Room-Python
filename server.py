import socket

# define the host and port to listen on
HOST = 'localhost'
PORT = 5555

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host and port
server_socket.bind((HOST, PORT))

# listen for incoming connections (backlog argument specifies the maximum number of queued connections)
server_socket.listen(1)
print('Chat room server started on {}:{}'.format(HOST, PORT))

# accept incoming connections
client_socket, address = server_socket.accept()
print('Connected to {}:{}'.format(address[0], address[1]))

while True:
    # receive data from the client
    data = client_socket.recv(1024).decode('utf-8')

    # if no data received, client has disconnected
    if not data:
        print('Client disconnected')
        break

    print('{}: {}'.format(address[0], data))

    # send the received data back to the client
    client_socket.sendall(data.encode('utf-8'))

# close the connection and the server
client_socket.close()
server_socket.close()
