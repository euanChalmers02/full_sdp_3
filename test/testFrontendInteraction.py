import unittest
# TODO: add assert statements here...
# exclude because requires interaction????
# still just to check they run...? Not the most useful...
from Main.fnd.SoundCode.Customisation import *
from fnd.SoundCode.SoundSys.VoiceToText import voice_wrapper


class interaction_tests(unittest.TestCase):
    def test_change_voice_property(self):
        change_voice_property(1)

    def test_update_type_of_beep(self):
        update_type_of_beep(0)

    def test_update_num_beeps(self):
        pass

    def test_select_an_option(self):
        select_an_option()

    def test_cycle_voices(self):
        cycle_voices()

    def test_cycle_beeps(self):
        cycle_beeps()

    def test_customise_number_beeps(self):
        customise_number_beeps()

    def test_voice_wrapper(self):
        voice_wrapper()