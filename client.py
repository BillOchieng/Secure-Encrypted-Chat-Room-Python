import socket

# define the host and port to connect to
HOST = 'localhost'
PORT = 5555

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))
print('Connected to {}:{}'.format(HOST, PORT))

while True:
    # send data to the server
    message = input('> ')
    client_socket.sendall(message.encode('utf-8'))

    # if no data sent, client has disconnected
    if not message:
        print('Disconnected from server')
        break

    # receive data from the server
    data = client_socket.recv(1024).decode('utf-8')

    # if no data received, server has disconnected
    if not data:
        print('Server disconnected')
        break

    print('Server: {}'.format(data))

# close the connection
client_socket.close()
