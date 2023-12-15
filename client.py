#!/home/sudharsan/myenv/bin/python3
import socket
import time
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = 'localhost'
port = 12457
client_socket.connect((host, port))
while True:
# Receive the welcome message from the server
    message = client_socket.recv(1024).decode('utf-8')
    if message:
        print(f"Received message from server: {message}")

# Close the connection with the server
client_socket.close()

