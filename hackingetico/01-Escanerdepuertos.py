import socket

#los puertos que deseas escanear
for puerto in range (70,80): 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    resultado = s.connect_ex('192.168.0.1',puerto)
    if resultado == 0:
        print(f'El puerto: {puerto} esta abierto')
    else:
        print(f'El puerto: {puerto} esta cerrado')