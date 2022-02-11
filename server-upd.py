import socket
import datetime as dt

localPort = 55555 #porta
portEnvio = 1080
bufferSize = 1024
endPortaEnvio = ('client-ip', 1080)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind(('local-ip',localPort))
print("UPD server is ready")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    msg = bytesAddressPair[0]
    endPorta = bytesAddressPair[1]

    msgdecode = msg.decode('UTF-8')
    recebido = msgdecode.split(' ')
    msgFormatada = bytes("ack: " + recebido[0], 'utf-8')
    UDPServerSocket.sendto(msgFormatada, endPorta)