import socket
import time


buffsize = 1024
# Multicast addresses range from 224.0.0.0 to 230.255.255.255
broadcastAddress = '255.255.255.255'
port = 4444

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set socket to sent broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

messageToSend = b"message\n"

while True:
    sock.sendto(messageToSend, (broadcastAddress, port))
    print("Broadcast message sent!")
    time.sleep(1)