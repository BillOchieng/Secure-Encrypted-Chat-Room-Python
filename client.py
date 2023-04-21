import socket
import json

# define the host and port of the server to connect to
HOST = 'localhost'
PORT = 5555

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))

# prompt the user to enter a username
username = input('Enter your username: ')

while True:
    # prompt the user to enter a chat message
    message = input('{}: '.format(username))

    # create a dictionary to store the username and message
    data = {'username': username, 'message': message}

    # convert the dictionary to a JSON string and send it to the server
    data_str = json.dumps(data)
    client_socket.sendall(data_str.encode('utf-8'))

    # receive the response data from the server as bytes
    response_data_bytes = b''
    while True:
        chunk = client_socket.recv(1024)
        response_data_bytes += chunk
        if not chunk:
            break

    # extract the last JSON response from the data received
    response_data_str = response_data_bytes.decode('utf-8')
    last_response_str = response_data_str.split('\n')[-2]
    response_data = json.loads(last_response_str)

    # print the response data
    print('{}: {}'.format(response_data['username'], response_data['message']))

# close the connection to the server
    client_socket.close()
