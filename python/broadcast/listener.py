import socket

bufferSize = 1024
port = 4444

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set socket to deal with broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Bind socket to all interfaces and port 4444
sock.bind(('', port))

while True:
    receivedMessage, senderAddress = sock.recvfrom(bufferSize)
    print(receivedMessage.decode("utf-8"), senderAddress)


