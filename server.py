import socket
import json

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

# open the chat log file in append mode
with open('chat_log.json', 'a') as f:
    while True:
        # receive data from the client as bytes
        data_bytes = client_socket.recv(1024)

        # if no data received, client has disconnected
        if not data_bytes:
            print('Client disconnected')
            break

        # decode the bytes as a string and load the JSON data
        data_str = data_bytes.decode('utf-8')
        data = json.loads(data_str)

        # print the received data
        print('{}: {}'.format(data['username'], data['message']))

        # add the message to the chat log file
        f.write(json.dumps(data) + '\n')

        # send the received data back to the client as JSON
        response_data = {'message': data['message'], 'username': 'Server'}
        response_data_str = json.dumps(response_data)
        client_socket.sendall(response_data_str.encode('utf-8'))

        # send a message to the client
        server_message = {'message': 'Hello, client!', 'username': 'Server'}
        server_message_str = json.dumps(server_message)
        client_socket.sendall(server_message_str.encode('utf-8'))

# close the connection and the server
server_socket.close()
