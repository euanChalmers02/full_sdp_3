import threading
import unittest
import time

from Main.fnd.SoundCode.Buttons.sysState import *
from Main.fnd.SoundCode.SoundSys.OCR import *
from Main.fnd.SoundCode.Buttons.ButtionChange import *

# helper func
def set_now():
    time.sleep(4)
    state.stop = True
    time.sleep(6)
    state.stop = False
    return

# class testOCR(unittest.TestCase):
    # def test_speach_OCR(self):
    #     # this should pause after 1.5 seconds of speech then resume after another 1sec
    #     thread_test = threading.Thread(target=set_now, args=())
    #     thread_test.start()
    #
    #     # this will kill after x amount of time instead of using keyboard inputs
    #     # thread_test_2 = threading.Thread(target=set_now, args=())
    #     # thread_test_2.start()
    #     print('Started Thread')
    #     xyz = "This is a test sentence that should run"
    #     rx = OCR(xyz)

    # def test_reading_long_phrase_with_buttons_thread(self):
    #
    #     obama_Speech = """Barack Obama: Words Matter. Don’t tell me words don’t matter. I have a dream – just words words. We hold
    #         these truths to be self evident that all men are created equal – just words. We
    #         have nothing to fear but fear itself – just words, just speeches.
    #         It’s true that speeches don’t solve all problems, but what is also true is that if
    #         we can’t inspire our country to believe again, then it doesn’t matter how many
    #         policies and plans we have, and that is why I’m running for president of the
    #         United States of America, and that’s why we just won 8 elections straight
    #         because the American people want to believe in change again. Don’t tell me
    #         words don’t matter! """
    #
    #     thread_test = threading.Thread(target=console, args=())
    #     thread_test.start()
    #
    #     # this will kill after x amount of time instead of using keyboard inputs
    #     # thread_test_2 = threading.Thread(target=set_now, args=())
    #     # thread_test_2.start()
    #     print('Started Thread')
    #     rx = OCR(obama_Speech)



if __name__ == '__main__':
    unittest.main()
