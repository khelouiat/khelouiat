import os  # importing os library so as to communicate with the system
import time  # importing time library to make Rpi wait because its too impatient
os.system("sudo pigpiod")  # Launching GPIO library
time.sleep(1)  # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio  # importing GPIO library
ESC = 4  # Connect the ESC in this GPIO pin
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)
max_value = 2000  # change this if your ESC's max value is different or leave it be
min_value = 700  # change this if your ESC's min value is different or leave it be
print("For first time launch, select calibrate")
print("Type the exact word for the function you want")
print("calibrate OR manual OR control OR arm OR stop")

 # This is the auto calibration procedure of a normal ESC
while True:
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC, min_value)
            print("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep(5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
            control()  # You can change this to any other function you want





# This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.

