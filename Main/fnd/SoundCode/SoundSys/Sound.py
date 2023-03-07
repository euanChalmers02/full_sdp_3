import numpy as np
import librosa
from scipy import signal
import sounddevice as sd
import os

from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state

state = get_instate_of_state()

# adjustable output parameters (add these to the setup class??)
from Main.fnd.SoundCode.SoundSys.Setup import *

# -- customisable --
beep_pause = 800  # ms (can we standardise these)
beep_duration = 0.3  # sec
beep_type = 'beep-07a.wav'

PATH = os.path.abspath(__file__)
ROOT = (PATH.split("Main"))[0] + "Main/fnd/"
# 3D sound file library https://www.york.ac.uk/sadie-project/database.html
D1_YORK_SRC_PATH = ROOT + 'D1_HRIR_WAV/44K_16bit'
BEEP_SOUND_PATH = ROOT + 'beeps/'

class Sound:
    # setup is currently a class variable
    setup = Setup(1280, 720, 79, 41)  # this should be cache and passed as an arg??? Not done due to unit tests
    # TODO: update what the newest camera params are.

    def __init__(self, coord, distance, text, beep): # distance float...
        self.coord = coord
        self.file = self.convert_to_file()
        # distance passed as float...
        self.distance = distance  # how to convey distance (increase frequency of beeps)
        self.text = text
        self.beep = beep

        self.front = None
        self.Bin_Max = None
        self.freq = None  # this will be either true or false

    def convert_to_file(self):
        angle, elev = Sound.setup.find_the_file_two(self.coord)

        if angle == 0:
            print('Bearing == 0. Flagged as \'front\'')
            self.front = True

        # dict for filenames with weird decimals
        diff_dict = {17: "17,5", 35: "35,3", 64: "64,8", -17: "-17,5", -35: "-35,3", -64: "-64,8"}
        if elev in diff_dict:
            elevation = diff_dict[elev]
        else:
            elevation = str(elev) + ',0'

        return '/azi_' + str(angle) + ',0_ele_' + elevation + '.wav'

    # spatial audio based on orientation only
    def create_3d(self):
        HRIR_RE, fs_H0 = librosa.load(D1_YORK_SRC_PATH + self.file, sr=48000, mono=False)
        [src_o, fs_s0] = librosa.load(BEEP_SOUND_PATH + beep_type, mono=True, sr=48000)
        # sr <== fps but sound

        s_0_L = signal.fftconvolve(src_o, HRIR_RE[0, :])  # source left
        s_0_R = signal.fftconvolve(src_o, HRIR_RE[1, :])  # right

        Bin_Max = np.vstack([s_0_L, s_0_R]).transpose()
        Bin_Max = Bin_Max / np.max(np.abs(Bin_Max))
        # final end product

        # ---------------------------------------
        # refactor this..
        pitch_scale  = self.convert_distance_freq()

        # Plays the sound within the control system loop
        self.Bin_Max = Bin_Max  # volume
        self.freq = fs_s0 * pitch_scale # pitch

    # play beep sound
    def play(self):
        if not self.beep:
            return

        temp = self.convert_distance_time()

        # used for light debugging
        if state.debug:
            print("self.Bin_Max, self.freq")
            print(self.Bin_Max, self.freq)

        sd.play(self.Bin_Max, self.freq)
        sd.sleep(int(beep_duration*temp))
        sd.stop()

    def get_name(self):
        return self.text

    def convert_distance_time(self):
        # get self.distance.
        if self.distance > 6:
            return 900
            # If the distance is between 50 and 30 cm, we will beep once a second
        elif self.distance <= 6 and self.distance >= 3:
            return 600
            # If the distance is between 30 and 20 cm, we will beep every twice a second
        elif self.distance < 3 and self.distance >= 1:
            return 400
            # If the distance is between 20 and 10 cm, we will beep four times a second
        elif self.distance < 1 and self.distance >= 0.5:
            return 100
            # If the distance is smaller than 10 cm, we will beep constantly
        else:
            return 100

    def convert_distance_freq(self):
        if self.distance > 8:
            return 0.9
        if self.distance <= 8 and self.distance > 6:
            return 1
            # If the distance is between 50 and 30 cm, we will beep once a second
        elif self.distance <= 6 and self.distance >= 3:
            return 1.25
            # If the distance is between 30 and 20 cm, we will beep every twice a second
        elif self.distance < 3 and self.distance >= 1:
            return 1.5
            # If the distance is between 20 and 10 cm, we will beep four times a second
        elif self.distance < 1 and self.distance >= 0.5:
            return 1.6
            # If the distance is smaller than 10 cm, we will beep constantly
        else:
            return 1.75
