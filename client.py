import socket
import threading

HOST = 'localhost'
PORT = 5005

def handle_input():
    while True:
        # Read input from the user
        message = input()
        # Send the message to the server
        client_socket.send(message.encode())

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

print(f'Connected to server at {HOST}:{PORT}')

# Start a new thread to handle user input
input_thread = threading.Thread(target=handle_input)
input_thread.start()

while True:
    # Receive data from the server
    data = client_socket.recv(1024)
    if not data:
        break
    # Print the received data
    print(f'Received: {data.decode()}')

client_socket.close()
