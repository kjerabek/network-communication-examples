import socket

# Multicast addresses range from 224.0.0.0 to 230.255.255.255
multicastAddress = '239.192.1.100'
port = 5555
ttl = 1
messageToSend = "message\n"

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set TTL to value
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

sock.sendto(messageToSend.encode(), (multicastAddress, port))

sock.close()