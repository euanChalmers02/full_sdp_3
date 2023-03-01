import threading
import time

from Main.fnd.SoundCode.Buttons.ButtionChange import *
from SoundSys.TextToSpeech import *
from SoundSys.Sound import *
from Main.fnd.SoundCode.SoundSys.OCR import *
from fnd.SoundCode.Customisation import select_an_option, customise_number_beeps


if __name__ == "__main__":
    obama_Speech = """Barack Obama: Words Matter.
               Don’t tell me words don’t matter. I have a dream – just words words. We hold
               these truths to be self evident that all men are created equal – just words. We
               have nothing to fear but fear itself – just words, just speeches.
               It’s true that speeches don’t solve all problems, but what is also true is that if
               we can’t inspire our country to believe again, then it doesn’t matter how many
               policies and plans we have, and that is why I’m running for president of the
               United States of America, and that’s why we just won 8 elections straight
               because the American people want to believe in change again. Don’t tell me
               words don’t matter! """

    thread_test = threading.Thread(target=console, args=())
    thread_test.start()

    # this will kill after x amount of time instead of using keyboard inputs
    # thread_test_2 = threading.Thread(target=set_now, args=())
    # thread_test_2.start()
    print('Started Thread')
    rx = OCR(obama_Speech)

    # text = "Hello world this is xyz"
    # textToSpeech(text)
    # obj1 = Sound([79, 470], 0, "Object 1. " + "Il Calcio bistro", True)
    #
    # customise_number_beeps()

    # obj2 = Sound([65, 291], 0, "Object 2. " , True)
    # obj3 = Sound([348, 195], 0, "Object 3. " , True)
    # obj4 = Sound([700, 279], 0, "Object 3. " , True)
    # obj5 = Sound([1076, 440], 0, "Object 3. " , True)
    # obj6 = Sound([937, 148], 0, "Object 3. " , True)
    # all_objects = [obj1, obj2, obj3, obj4, obj5, obj6]
    #
    # for o in all_objects:
    #     # print(o.get_name())
    #     o.create_3d()
    #     for _ in range(3):
    #         o.play()
    #     time.sleep(0.5)

    # sound_action(obj1, [])

    # voice_wrapper()
    #
    # select_an_option()

    # save_msg_to_cache('Qutting', "Qutting")
    # save_msg_to_cache('How many beeps would you like to play, please say the number now.', 'customise_beeps_start')
    # save_msg_to_cache('Great updating now.', "Great_Updating_Now")
    # save_msg_to_cache('Sorry, Please Say your number again or say quit.', "say_again")
    # save_msg_to_cache('Please say the number of the voice you would like.', 'voice_number_start')
    # save_msg_to_cache('Please say the number of the beep sound you would like.', 'beep_type_start')

    start = time.time()
    # save_msg_to_cache('Test sentence to check speed', "test_phrase")
    # play_msg_cache("test_phrase")
    #
    # engine = pyttsx3.init()
    # engine.say('Test sentence to check speed')
    # engine.runAndWait()

    print('Total time is', time.time() - start)