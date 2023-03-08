import threading
import time
import random

from fnd.SoundCode.Buttons.ButtionChange import console_two
from fnd.SoundCode.Buttons.sysState import next_mode

if __name__ == "__main__":
    print(next_mode("voice"))

    # first iteration of the multi object capture
    # dict_i = {"name":name,"coord":10202}
    # L = [dict_i,dict_i,dict_i]
    # print(L)
    # xr = list({v['name']:v for v in L}.values())
    # print(xr)


    # class StateManger(object):
    #     _instance = None
    #     no_beeps = 3
    #     pause_length = 1
    #     all_objects = []
    #     sysState = "Scan"
    #     id = random.randint(0, 1000)
    #
    #     def __init__(self):
    #         raise RuntimeError('Call instance() instead')
    #
    #     @classmethod
    #     def instance(cls):
    #         if cls._instance is None:
    #             print('Creating new instance')
    #             cls._instance = cls.__new__(cls)
    #         return cls._instance
    #
    #     def get_id(self):
    #         return id
    #
    #     def update_state(self,sts):
    #         sysState = sts
    #
    #
    #
    # lg = StateManger.instance()
    # print(lg.id)
    # print(lg.update_state("scan+"))
    # print(lg.sysState)





    # how to fake setup the state -> using another thread??


    #     if closer = true then will reduce else will get further away until limit reached


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

    # start = time.time()
    # save_msg_to_cache('Test sentence to check speed', "test_phrase")
    # play_msg_cache("test_phrase")
    #
    # engine = pyttsx3.init()
    # engine.say('Test sentence to check speed')
    # engine.runAndWait()

    # print('Total time is', time.time() - start)