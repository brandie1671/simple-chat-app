import socket
import threading

HOST = 'localhost'
PORT = 5005

def handle_client(client_socket, address):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        # Print the received data
        print(f'Received from {address[0]}:{address[1]}: {data.decode()}')
        # Send the received data back to all connected clients
        for c in clients:
            c.send(data)
    # Remove the client from the list of connected clients
    clients.remove(client_socket)
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}')

# Create an empty list to store connected clients
clients = []

while True:
    # Accept a new client connection
    client_socket, address = server_socket.accept()
    print(f'Client connected from {address[0]}:{address[1]}')
    # Add the new client to the list of connected clients
    clients.append(client_socket)
    # Start a new thread to handle the client's messages
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
