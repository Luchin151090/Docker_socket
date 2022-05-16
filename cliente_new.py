import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
print("Enviar la funcion lim_inf lim_sup N")
message = input()#b'NUESTRO MENSAJE' 90

try:
    # Send data
    #casteo
    message=bytes(message,'utf-8')
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()