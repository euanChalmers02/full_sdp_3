import sys

if sys.platform != "darwin":
    import RPi.GPIO as GPIO

import cv2
import pyaudio
import serial
import threading
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def check_system():
    print(bcolors.WARNING + "Starting System Checks" + bcolors.ENDC)
    all_func = [check_buttons,check_depth,check_camera,check_audio]
    for act in all_func:
        # thread_check = threading.Thread(target=act)
        print("-" * 20)
        try:
            act()
        except:
            print("Failed -> ",act)

def check_buttons():
    # check buttons
    # set up GPIO pins
    try:
        GPIO.setmode(GPIO.BOARD)
        # define button pins
        button1_pin = 16
        button2_pin = 18
        button3_pin = 22

        # set up button pins as input with pull-up resistors
        GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print(bcolors.OKGREEN + "buttons GOOD" + bcolors.ENDC)
        return True
    except:
        print(bcolors.FAIL + "buttons BAD" + bcolors.ENDC)
        return False

def check_depth():
#     check serial
    try:
        ser = serial.Serial("/dev/serial0", 115200, timeout=0)  # mini UART serial device
        if ser.isOpen() == False:
            ser.open()  # open serial port if not open
            print(bcolors.OKGREEN + "depth sensor GOOD" + bcolors.ENDC)
        return True
    except:
        print(bcolors.FAIL + "depth sensor BAD" + bcolors.ENDC)
        return False

# check camera
def check_camera():
    try:
        capture = cv2.VideoCapture(0)
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # print("Camera specs -> ", width, "-", height)
        # print("-" * 20)
        capture.release()
        cv2.destroyAllWindows()
        print(bcolors.OKGREEN + "camera GOOD" + bcolors.ENDC)
        return True

    except:
        print(bcolors.FAIL + "camera BAD" + bcolors.ENDC)
        return False

def check_audio():
    # print("-"*20)
    # print("Default Audio Devices")
    # print("-" * 20)
    p = pyaudio.PyAudio()
    try:
        mic = p.get_default_input_device_info()
        spk = p.get_default_output_device_info()
        # print("-" * 20)
        # print("PyAudio default input->", mic["name"], " -> Index = ", mic["index"])
        # print("PyAudio default output->", spk["name"], " -> Index = ", spk["index"])
        # print("-" * 20)
        print(bcolors.OKGREEN + "audio GOOD" + bcolors.ENDC)
        return True
    except:
        print(bcolors.FAIL + "audio BAD" + bcolors.ENDC)
        return False


if __name__ == '__main__':
    check_system()