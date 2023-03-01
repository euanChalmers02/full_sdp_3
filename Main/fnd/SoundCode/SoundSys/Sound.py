import numpy as np
import librosa
from scipy import signal
import sounddevice as sd
import os

# adjustable output parameters (add these to the setup class??)
from Main.fnd.SoundCode.SoundSys.Setup import *

# -- customisable --
beep_pause = 800  # ms (can we standardise these)
beep_duration = 0.4  # sec
beep_type = 'beep-07a.wav'
# engine = pyttsx3.init()
# engine.setProperty('rate', 400)

PATH = os.path.abspath(__file__)
ROOT = (PATH.split("Main"))[0] + "Main/fnd/"
# 3D sound file library https://www.york.ac.uk/sadie-project/database.html
D1_YORK_SRC_PATH = ROOT + 'D1_HRIR_WAV/44K_16bit'
BEEP_SOUND_PATH = ROOT + 'beeps/'

class Sound:
    # setup is currently a class variable
    setup = Setup(1280, 720, 79, 41)  # this should be cache and passed as an arg??? Not done due to unit tests
    # TODO: update what the newest camera params are.

    def __init__(self, coord, distance, text, beep):
        self.coord = coord
        self.file = self.convert_to_file()
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

        s_0_L = signal.fftconvolve(src_o, HRIR_RE[0, :])  # source left
        s_0_R = signal.fftconvolve(src_o, HRIR_RE[1, :])  # right

        Bin_Max = np.vstack([s_0_L, s_0_R]).transpose()
        Bin_Max = Bin_Max / np.max(np.abs(Bin_Max))
        # final end product

        # Plays the sound within the control system loop
        self.Bin_Max = Bin_Max
        self.freq = fs_s0

    # play beep sound
    def play(self):
        if not self.beep:
            return

        sd.play(self.Bin_Max, self.freq, blocking=True)

    def get_name(self):
        return self.text
