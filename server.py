#!/home/sudharsan/myenv/bin/python3
import socket
import keyboard
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = 'localhost'
port = 12457
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on {host}:{port}")
client_socket, addr = server_socket.accept()
print(f"Got connection from {addr}")

def send(message):
    # Send a welcome message to the client
    client_socket.send(message.encode('utf-8'))

def on_key_event(e):
    global a
    if (e.event_type == keyboard.KEY_DOWN):
        send(e.name)

l=keyboard.hook(on_key_event)
keyboard.wait('esc')  # Wait for the 'esc' key to be pressed to exit the program






    # Close the connection with the client
client_socket.close()

