import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BOARD)

# define button pins
button1_pin = 11
button2_pin = 13
button3_pin = 15

# set up button pins as input with pull-up resistors
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# define button state variables
button1_state = False

# define long press time in seconds
long_press_time = 2

def switchOnOff(channel):
    global button1_state
    start_time = time.time()
    while GPIO.input(channel) == GPIO.LOW:
        if (time.time() - start_time) > long_press_time:
            button1_state = not button1_state
            print("button1 is long pressed")
            break


def switchMode(channel):
    if GPIO.input(channel) == GPIO.LOW:
        print("switch button1 mode")

def increaseVolume(channel):
    if GPIO.input(channel) == GPIO.LOW:
        print("button2d is pressed, increase volume")

def decreaseVolume(channel):
    if GPIO.input(channel) == GPIO.LOW:
        print("button3 is pressed, decrease volume")

# add event detection
GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=switchOnOff, bouncetime=300)
GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=switchMode, bouncetime=300)
GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=increaseVolume, bouncetime=300)
GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=decreaseVolume, bouncetime=300)


