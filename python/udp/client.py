import socket

bufferSize = 1024
messageToSend = "message\n"
ip = "127.0.0.1"
port = 6666

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to specific IP and port
sock.sendto(messageToSend.encode(), (ip, port))

# Wait for receiving the message
receivedMessage, senderAddress = sock.recvfrom(bufferSize)

print(receivedMessage.decode("utf-8"), senderAddress)