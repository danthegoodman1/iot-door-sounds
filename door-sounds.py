import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
import os
from subprocess import call
import random
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#while True: # Run forever
 #   if GPIO.input(10) == GPIO.HIGH:
  #      print("Button was pushed!")
   #     sleep(0.2)

playing = False # variable so we dont play a sound a million times when the door opens

# Get the different sound lists



# Connect to websocket
while True:
#     Parent if statement for socket to determine what mode
    volumeLevel = 106555
    if (GPIO.input(10) == False and playing == False):
        randomSound = random.choice(os.listdir('/home/pi/sounds/')) # pick a random song
        print(randomSound)
        playing = True
        os.system('mpg123 -q /home/pi/sounds/' + randomSound + ' -f ' + volumeLevel + ' --scale ' + volumeLevel + ' &')
        sleep(5)
        playing = False
