import RPi.GPIO as GPIO
import cv2
import pyaudio


def check_hardware():
    # check buttons
    # set up GPIO pins
    GPIO.setmode(GPIO.BOARD)
    # define button pins
    button1_pin = 16
    button2_pin = 18
    button3_pin = 22
    try:
        # set up button pins as input with pull-up resistors
        GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    except:
        print("buttons not connected")

#     check serial
    try:
        ser = serial.Serial("/dev/serial0", 115200, timeout=0)  # mini UART serial device
        if ser.isOpen() == False:
            ser.open()  # open serial port if not open
    except:
        print("depth sensor not connected")

# check camera

    try:
        capture = cv2.VideoCapture(0)
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Camera specs -> ", width, "-", height)
        print("-" * 20)
        capture.release()
        cv2.destroyAllWindows()

    except:
        print("camera not connected correctly ")


    print("-"*20)
    print("Default Audio Devices")
    print("-" * 20)
    p = pyaudio.PyAudio()
    try:
        mic = p.get_default_input_device_info()
        spk = p.get_default_output_device_info()
        print("-" * 20)
        print("PyAudio default input->", mic["name"], " -> Index = ", mic["index"])
        print("PyAudio default output->", spk["name"], " -> Index = ", spk["index"])
        print("-" * 20)
    except:
        print("No mics availiable")