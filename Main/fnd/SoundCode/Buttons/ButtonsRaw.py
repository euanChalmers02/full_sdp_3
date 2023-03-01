#
# Skeleton for Raspberry Pi button config
#

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel):
    print("Button was pushed! ",channel)


# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/
GPIO.setmode(GPIO.BOARD)
GPIO.setup(17,GPIO.IN)

# add each for each button to handle -> how to sense double click
input_button = GPIO.input(17)


# -------------------- other option ------------------------------

from gpiozero import Button

def say_hello():
    print("Hello!")

btn = Button(17)
btn_two = Button(10)
btn_three = Button(12)

# this should catch a double click how to make it work for each button / parrallel process??
while True:
    btn.wait_for_press()
    btn.wait_for_release()
    if btn.wait_for_press(timeout=0.6):
        print("pressed twice")
    else:
        print("single click")

