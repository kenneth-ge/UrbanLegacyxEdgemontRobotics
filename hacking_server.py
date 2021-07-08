# We will need the following module to generate randomized lost packets
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    message = message.decode()
    print(message)

    if message == 'get * from table':
        # send password
        serverSocket.sendto("LgXM3YiCTihFM3DnX3Ac2a37sjN".encode(), address)
    else:
        serverSocket.sendto('forbidden'.encode(), address)
