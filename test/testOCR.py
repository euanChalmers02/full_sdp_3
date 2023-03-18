import threading
import unittest
import time

from Main.Main.fnd.SoundCode.Buttons.sysState import *
from Main.Main.fnd.SoundCode.SoundSys.OCR import *
from Main.Main.fnd.SoundCode.Buttons.ButtonChange import *

# helper func
# def set_now():
#     time.sleep(4)
#     state.stop = True
#     time.sleep(6)
#     state.stop = False
#     return
from Main.Main.OCR_PERCEPTION.basic import get_text


class testOCR(unittest.TestCase):
    # def test_speach_OCR(self):
    #     # this should pause after 1.5 seconds of speech then resume after another 1sec
    #     # thread_test = threading.Thread(target=set_now, args=())
    #     # thread_test.start()
    #
    #     # this will kill after x amount of time instead of using keyboard inputs
    #     # thread_test_2 = threading.Thread(target=set_now, args=())
    #     # thread_test_2.start()
    #     print('Started Thread')
    #     xyz = "This is a test sentence that should run"
    #     rx = OCR(xyz)
    #
    #     # thread_test.join(6)
    #
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
    #     thread_test = threading.Thread(target=console_two, args=())
    #     thread_test.start()
    #
    #     thread_test.join(6)
    #
    #     # this will kill after x amount of time instead of using keyboard inputs
    #     thread_test_2 = threading.Thread(target=set_now, args=())
    #     thread_test_2.start()
    #     print('Started Thread')
    #     rx = OCR(obama_Speech)

    def test_text_size_1(self):
        text = get_text("test_images/size1.jpeg")

        self.assertEqual("OXFORD\n“STREET WI\n\nCITY OF WESTMINSTER\n\n", text)

    def test_font_1(self):
        text = get_text("test_images/font1.png")

        self.assertEqual("THE UNIVERSITY\nof EDINBURGH\n\n", text)

    def test_font_2(self):
        text = get_text("test_images/font2.jpeg")

        # should really regex it, but no time
        self.assertEqual("| Wandered Lonely“as) a) Cloud\n\n~William)Wordsworth\n\n", text)


if __name__ == '__main__':
    unittest.main()
