import RPi.GPIO as GPIO
import time
from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
from Main.fnd.SoundCode.Logging import add_log, TypeLogs

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
            add_log("Button AA pressed", TypeLogs.TESTING)
            print("button AA is long pressed")
            state.commandInterface('AA')
        else:
            add_log("Button A pressed", TypeLogs.TESTING)
            print("button A is not long pressed")
            state.commandInterface('A')


def increaseVolume(channel):
    global start
    global end
    if GPIO.input(channel) == 1:
        start = time.time()
    if GPIO.input(channel) == 0:
        end = time.time()
        elapsed = end - start
        print(elapsed)
        if elapsed > long_press_time:
            add_log("Button BB pressed", TypeLogs.TESTING)
            print("button BB is long pressed")
            state.commandInterface('BB')
        else:
            add_log("Button B pressed", TypeLogs.TESTING)
            print("button B is not long pressed")
            state.commandInterface('B')


def decreaseVolume(channel):
    global start
    global end
    if GPIO.input(channel) == 1:
        start = time.time()
    if GPIO.input(channel) == 0:
        end = time.time()
        elapsed = end - start
        print(elapsed)
        if elapsed > long_press_time:
            print("button CC is long pressed")
            add_log("Button CC pressed", TypeLogs.TESTING)
            state.commandInterface('CC')
        else:
            add_log("Button C pressed", TypeLogs.TESTING)
            print("button CC is short pressed")
            state.commandInterface('C')


def buttons_console():
    print('run')
    # add event detection
    GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback=switchOnOff, bouncetime=300)
    GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=increaseVolume, bouncetime=300)
    GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=decreaseVolume, bouncetime=300)
    message = input("Press enter to quit\n\n")
    print(message)
    GPIO.cleanup()
