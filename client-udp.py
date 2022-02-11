#codigo configurado na maquina de weslley
import socket
from typing import ByteString
import threading
import time

serverAddressPort = ('server-ip', 50005)

bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def envia():
    global inputClient
    inputClient = ''
    global countmsg
    countmsg = 0
    inputClient = ""
    while (inputClient != 'quit'):
        while True:
            if(countmsg < 30):
                inputClient = input()
                msgFromClient = bytes(str(countmsg + 1) +' '+inputClient, 'utf-8')
                UDPClientSocket.sendto(msgFromClient, serverAddressPort)
                countmsg = countmsg + 1
                intervalomsg = countmsg % 10
                if(intervalomsg == 0 and countmsg != 0):
                    print("10 seconds interval")
                    time.sleep(10)
                    if(countmsg == 30):
                        break
                
def recebe():
    UDPClientSocket.bind(('client-ip', 34942))
    countAck=0
    while True:
        if(countmsg < 30):
            msgServidor = UDPClientSocket.recvfrom(1024)
            print("Server message: {}".format(msgServidor[0].decode('utf-8')))
            msgServidor = msgServidor[0].decode('utf-8')
            msgAck = msgServidor.find('ack')
            
            if(msgAck != -1): #-1 ack nao encontrado
                countAck = countAck + 1
            if(countmsg == 30):
                taxaPerda = (countmsg-countAck)/countmsg
                print('Lost rate: ', taxaPerda)
                UDPClientSocket.close()
            

enviar = threading.Thread(target=envia)
receber = threading.Thread(target=recebe)

receber.start()
enviar.start()