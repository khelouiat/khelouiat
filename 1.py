import time
import socket
import random
UDP_IP = "192.168.1.100"
UDP_PORT = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, 0)
final =''
while True:
    roll = random.randrange(1,100)
    a = str(roll)
    s.sendto(a.encode('utf-8'), (UDP_IP, UDP_PORT))
    data, address = s.recvfrom(2048)
    data = data.decode("utf-8")
    final = data.split(',');
    print( final[0])

