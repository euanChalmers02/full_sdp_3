import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BOARD)

# define button pins
button1_pin = 16
button2_pin = 18
button3_pin = 22

# set up button pins as input with pull-up resistors
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# define button state variables
button1_state = False

from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
state = get_instate_of_state()

# define long press time in seconds
long_press_time = 2

def switchOnOff(channel):
    global start
    global end
    if GPIO.input(channel) == 1:
        start = time.time()
    if GPIO.input(channel) == 0:
        end = time.time()
        elapsed = end - start
        print(elapsed)
        if elapsed > long_press_time:
            print("button1 is long pressed")
            state.commandInterface('1')
        else:
            print("button1 is not long pressed")
            state.commandInterface('2')
            

def increaseVolume(channel):
    print("button2 is pressed, increase volume")
    state.commandInterface('3')
def decreaseVolume(channel):
    print("button3 is pressed, decrease volume")
    state.commandInterface('4')


def buttons_console():
    print('run')
    # add event detection
    GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback=switchOnOff, bouncetime=300)
    GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=increaseVolume, bouncetime=300)
    GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=decreaseVolume, bouncetime=300)
    message = input("Press enter to quit\n\n")
    GPIO.cleanup()

