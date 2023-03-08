from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
from Main.fnd.SoundCode.SoundSys.Sound import Sound
import serial,time
state = get_instate_of_state()

# ----------------------------FAKE----------------------------------
class Fake_Sensor:
    def __init__(self, start, closer, increment):
        self.index = 0
        arr_pos = []
        pos = start
        while 8 > pos and pos > 0:
            if closer:
                pos = pos - increment
            else:
                pos = pos + increment
            if pos > 0 and pos < 8:
                arr_pos.append(round(pos, 3))
        self.arr_pos = arr_pos

    def sensor(self):
        x = self.arr_pos[self.index]
        self.index = self.index + 1
        if self.index > len(self.arr_pos):
            self.index = 0
        return x





# ----------------------------END OF FAKE --------------------------


def read_tfluna_data():
    while True:
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = ser.read(9) # read 9 bytes
            ser.reset_input_buffer() # reset buffer

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256 # distance in next two bytes
                strength = bytes_serial[4] + bytes_serial[5]*256 # signal strength in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7]*256 # temp in next two bytes
                temperature = (temperature/8.0) - 256.0 # temp scaling and offset
                return distance/100.0,strength,temperature


ser = serial.Serial("/dev/serial0", 115200,timeout=0) # mini UART serial device
if ser.isOpen() == False:
    ser.open() # open serial port if not open


def get_dist():
    distance,strength,temperature = read_tfluna_data() # read values
    print('Distance func: {0:2.2f} m, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'.\
              format(distance,strength,temperature)) # print sample data
              
    return distance




# this is the driver code for the distance and should be pointed to by a thread or treated as a state
def distance_action_or_state():
    # this would connect to the sensor?? but will create the fake sensor here
    #fs = Fake_Sensor(7, True, 0.5)

    # should keep going until a button is pressed
    print("state.get_state()  ",state.get_state(), "id is ",state.id)
    while state.get_state() == "dist":
        print('run ...')
        # fs.sensor() is the distance sensor response
        dist = get_dist()
        print('distance got ',dist) 
        # how to play the sound using distance here

        # this uses the exact middle of the frame that should be calibrated and stored centrally
        middle = [1280 / 2, 720 / 2]

        o = Sound(middle,dist, "", True)
        o.create_3d()
        o.play()
