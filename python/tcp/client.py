import socket

bufferSize = 1024
messageToSend = "message\n"
ip = "127.0.0.1"
port = 6666

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create connection with specific IP and port
sock.connect((ip, port))

# Send data
sock.send(messageToSend.encode())

# Wait for receiving data
receivedMessage = sock.recv(bufferSize)

print(receivedMessage.decode("utf-8"))

sock.close()