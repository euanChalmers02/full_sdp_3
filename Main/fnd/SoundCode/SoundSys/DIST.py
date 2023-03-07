from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
from fnd.SoundCode.SoundSys.Sound import Sound
from Main.fnd.SoundCode.Buttons.ButtionChange import *
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

# this is the driver code for the distance and should be pointed to by a thread or treated as a state
def distance_action_or_state():
    # this would connect to the sensor?? but will create the fake sensor here
    fs = Fake_Sensor(7, True, 0.5)

    # should keep going until a button is pressed
    print("state.get_state()  ",state.get_state(), "id is ",state.id)
    while state.get_state() == "dist":
        print('run ...')
        # fs.sensor() is the distance sensor response
        dist = fs.sensor()
        # how to play the sound using distance here

        # this uses the exact middle of the frame that should be calibrated and stored centrally
        middle = [1280 / 2, 720 / 2]

        print("dist",dist)
        o = Sound(middle,dist, "", True)
        o.create_3d()
        o.play()
