import unittest

from Main.Main.fnd.SoundCode.SoundSys.TextToSpeech import save_msg_to_cache, play_msg_cache

# TODO: add assert statements here...

class sound_sys_tests(unittest.TestCase):
    def test_save_msg_to_cache(self):
        save_msg_to_cache('Pause this now pls', 'pause')

    def test_play_msg_cache(self):
        play_msg_cache('Lifts.wav')

if __name__ == '__main__':
    unittest.main()
