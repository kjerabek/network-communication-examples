import socket

bufferSize = 1024
messageToSend = "message\n"
ip = "0.0.0.0"
port = 6666

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket to (0.0.0.0) all interfaces/IPs and port
sock.bind((ip, port))

while True:
    receivedMessage, senderAddress = sock.recvfrom(bufferSize)

    print(receivedMessage.decode("utf-8"), senderAddress)

    sock.sendto(receivedMessage.encode(), senderAddress)