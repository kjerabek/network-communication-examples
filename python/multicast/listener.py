import socket
import struct

bufferSize = 1024
# Multicast addresses range from 224.0.0.0 to 230.255.255.255
multicastAddress = '239.192.1.100'
port = 5555

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to listeners address and port
sock.bind((multicastAddress, port))

# Add socket to the multicast group
group = socket.inet_aton(multicastAddress)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


while True:
    receivedMessage, senderAddress = sock.recvfrom(bufferSize)
    print(receivedMessage.decode("utf-8"), senderAddress)

