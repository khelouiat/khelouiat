from socket import *
import threading
import os    
import time
os.system ("sudo pigpiod")
time.sleep(1) 
import pigpio

address = ('192.168.1.200', 5000)  # Defind who you are talking to (must match arduino IP and port)
client_socket = socket(AF_INET, SOCK_DGRAM)  # Set Up the Socket
client_socket.settimeout(1)  # only wait 1 second for a resonse
rec_data=''
final =''

ESC = 17
ESC1= 18

Count_ESC = [ESC,ESC1]
pi = pigpio.pi();
pi.set_servo_pulsewidth(17, 1500)
pi.set_servo_pulsewidth(18, 1500)
time.sleep(2)

def data():
    while (1):  # Main Loop
      

       data = "1"  # Set data to Blue Command
       client_socket.sendto(str.encode(data), address)  # send command to arduino
       try:
           
           rec_data, addr = client_socket.recvfrom(2048)  # Read response from arduino
           rec_data = rec_data.decode("utf-8")
           final  = rec_data.split(',');

           #final1=final.split(b" " );
       # print() # Print the response from Arduino
         
           #  print(final[1])
           # print(final[3])
           #print(final1[1])
           #print(rec_data)
         
           pi.set_servo_pulsewidth(17, final[0])
           pi.set_servo_pulsewidth(18, final[1])
           print( final[1])
           print( final[0])
           
       except:
        pass


#POSITION = threading.Thread(target=data)
data().start()


    # time.sleep(2)  # delay before sending next command
