import unittest

from Main.Main.fnd.SoundCode.SoundSys.Setup import *
from Main.Main.fnd.SoundCode.SoundSys.TextToSpeech import play_msg_cache, save_msg_to_cache


class testSound(unittest.TestCase):
    setup = Setup(640, 360, 55, 35)

    def test_setup(self):
        setup = Setup(1280, 720, 79, 41)

    def test_closest_value_mid(self):
        setup = Setup(640, 360, 55, 35)
        hor_vals = [0, 11, 22, 34, 45, 56, 67, 79, 90, 101, 112, 124, 135, 146, 157, 168, 180, 191, 202, 213, 225, 236, 247, 258, 269, 281, 292, 303, 314, 326, 337, 348, 359, 371, 382, 393, 404, 415, 427, 438, 449, 460, 472, 483, 494, 505, 516, 528, 539, 550, 561, 573, 584, 595, 606, 618, 629]
        computed_idx = closest_value_index(hor_vals, 200)

        self.assertEqual(18, computed_idx)

    def test_find_the_file_two_1(self):
        val1, val2 = testSound.setup.find_the_file_two([0,0])

        assert(0, val1)
        assert(0, val2)

    def test_find_the_file_two_2(self):
        val1, val2 = testSound.setup.find_the_file_two([640,360])

        self.assertEqual(332, val1)
        self.assertEqual(-25, val2)

    def test_find_the_file_two_3(self):
        val1, val2 = testSound.setup.find_the_file_two([200,142])

        self.assertEqual(10, val1)
        self.assertEqual(15, val2)

    def test_save_msg_to_cache(self):
        save_msg_to_cache("Well well well, hi there.", "test_msg")

    def test_play_msg_cache(self):
        play_msg_cache("front.wav")

    def test_play_unknown_msg(self):
        play_msg_cache("twig")