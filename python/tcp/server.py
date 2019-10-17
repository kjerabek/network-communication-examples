import socket

bufferSize = 1024
messageToSend = "message\n"
ip = "0.0.0.0"
port = 6666

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to (0.0.0.0) all interfaces/IPs and port
sock.bind((ip, port))

# Set listen queue to 1
sock.listen(1)

while True:
    # Accept the incoming connection
    connection, senderAddress = sock.accept()

    connection.recv(bufferSize)

    connection.send(messageToSend.encode())

    connection.close()
