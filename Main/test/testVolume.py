import unittest

from Main.fnd.SoundCode.Customisation import *
from Main.fnd.SoundCode.SoundSys.Sound import Sound

obj1 = Sound([245, 188], 2, "toilet_sign", True)


class sound_sys_tests(unittest.TestCase):
    def test_up_1(self):
        # given
        update_level_to("mac", 5)
        # when
        audio_driver_up()
        # then
        assert(int(get_audio_level("mac"))== 86)

    def test_down_1(self):
        # given
        update_level_to("mac", 5)
        # when
        audio_driver_down()
        # then
        assert (int(get_audio_level("mac"))== 57)

    def test_up_2(self):
        # given
        update_level_to("mac", 71)
        # when
        audio_driver_up()
        audio_driver_up()
        # then
        self.assertTrue(int(get_audio_level("mac"))==100)

    def test_down_2(self):
        # given
        update_level_to("mac", 5)
        # when
        audio_driver_down()
        audio_driver_down()
        # then
        assert(int(get_audio_level("mac"))== 43)

    def test_up_at_max(self):
        # given
        update_level_to("mac", 100)
        # when
        audio_driver_up()
        # then
        assert (int(get_audio_level("mac"))==100)

    def test_down_at_min(self):
        # given
        update_level_to("mac", 0)
        # when
        audio_driver_down()
        # then
        assert (int(get_audio_level("mac"))==0)

    def test_with_sound(self):
        # given
        update_level_to("mac", 100)
        # play_msg_cache('Lifts.wav')
        # when
        audio_driver_down()
        audio_driver_down()
        audio_driver_down()
        # then
        # play_msg_cache('Lifts.wav')
        assert(int(get_audio_level("mac"))== 57)

    # def test_with_sound2(self):
    #     # given
    #     update_level_to("mac", 3)
    #     play_msg_cache('Lifts.wav')
    #     # when
    #     audio_driver_up()
    #     audio_driver_up()
    #     audio_driver_up()
    #     # then
    #     play_msg_cache('Lifts.wav')
    #     assert (int(get_audio_level("mac"))== 86)
