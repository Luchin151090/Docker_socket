import re
import socket
import sys
import logging
import time
from concurrent.futures import ThreadPoolExecutor
logging.basicConfig(level=logging.DEBUG,format='%(threadName)s:%(message)s')

funcion_general = ''
suma = 0.0
delta = 0.0
i = 0
def funcion(x):
    time.sleep(1)
    #Escribimos la funcion original
    logging.info(eval(funcion_general))
    return eval(funcion_general)
def sumar_trapecio(a,n):
    global suma
    global delta
    global i
    x_i = a + i * (delta)
    
    if (i == 0 or i == n):
       
        suma = suma + (1 * funcion(x_i))
    else:
        
        suma = suma + (2 * funcion(x_i))
   

def integral_aproximada(a,b,n):

    inicio = time.time()

    global suma
    global delta
    global i
    delta=(b-a)/n
    executor = ThreadPoolExecutor(max_workers=int(n/2))
    for i in range(0,n+1):
        executor.submit(sumar_trapecio(a,n))

    resultado=suma*(delta/2)
    fin = time.time()
    total_tiempo =fin-inicio
    return {'Area:':resultado,'Time:':total_tiempo}

def split_message(x):
    print("dentro de hola")
    cadena = str(x,'UTF-8')
    expresion = re.split(r'\s+',cadena)
    global funcion_general
    funcion_general= expresion[0]
    lim_inf = int(expresion[1])
    lim_sup = int(expresion[2])
    N = int(expresion[3])
    print(integral_aproximada(lim_inf,lim_sup,N))



####################### CONFIGURACION #####################
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

######################### LISTENING #######################
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    split_message(data)
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
