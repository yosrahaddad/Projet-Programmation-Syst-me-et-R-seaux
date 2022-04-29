from socket import *
from tkinter import *

client = socket(AF_INET, SOCK_STREAM)
host = '172.18.2.61' #gethostbyname(gethostname()) 
port = 4803
ADDR = (host, port)
client.connect(ADDR)


def send_request(ref, typ, val):
    msg = ref + ' ' + typ + ' ' + str(val)
    client.send(msg.encode('ascii'))
    return typ


def recv_facture():
    print("[RECEIPT IF IT EXISTS]")
    data = client.recv(1024).decode('ascii')
    print(data)
    return 0


# Senario client
print("[CLIENT STARTING] ...")
type = send_request('3000', 'ajout', 50)
if (type == 'retrait'):
    recv_facture()
print("[EXITING]..")
