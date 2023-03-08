from Main.fnd.SoundCode.SoundSys.VoiceToText import voice_wrapper_action
from Main.fnd.SoundCode.SoundSys.DIST import distance_action_or_state
from Main.fnd.SoundCode.Logging import *
from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
# import RPi.GPIO as GPIO
import time

state = get_instate_of_state()

def console_two():
    flag = True
    print('thread started')
    while flag:
        try:
            cmd = input('>')
            state.commandInterface(cmd)
        except EOFError as e:
            print(e)


def pause_wait_action():
    #save_logs_to_file()
    while state.get_state() == "pause":
        time.sleep(1)

    print('--> Resume scan')


def check_next_func():
    next_func = {"pause": pause_wait_action, "dist": distance_action_or_state, "voice": voice_wrapper_action}
    act = next_func[state.get_state()]
    if act is not None:
        return act
    else:
        print("could not find next command")
        return None

# --------------------------------BUTTONS ----------------------------------------
button1_pin = 11
button2_pin = 13
button3_pin = 15
pin_out_list = {}
# def catch_all_callback(channel):
#     if GPIO.input(channel) == GPIO.LOW:
#         print("Button pressed")
#         cmd = pin_out_list[channel]
#         state.commandInterface(cmd)
#     return
#
#
# def button_setup():
#     # set up GPIO pins
#     GPIO.setmode(GPIO.BOARD)
#
#     # set up button pins as input with pull-up resistors
#     GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
# def button_listening():
#     # add event detection
#     GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=catch_all_callback, bouncetime=300)
#     GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=catch_all_callback, bouncetime=300)
#     GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=catch_all_callback, bouncetime=300)
#     GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=catch_all_callback, bouncetime=300)
