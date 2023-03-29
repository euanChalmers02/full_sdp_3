import json
import os

from Main.fnd.SoundCode.SoundSys.TextToSpeech import *

if __name__ == "__main__":
    from Main.fnd.SoundCode.SoundSys.OCR import *

    text = " Hello world " \
           "" \
           "" \
           ""
    OCR(text)


    OCR("this is a second one")
    # save_msg_to_cache("Vision Eddd is a headset for visually impaired users to identify the common signs in their environment. VisionED detected what the sign is and then orientates the user using spatial audio. VisionED headset has 3 modes","video")
    # play_msg_cache('video')


    # # # repsonsive test handling system
    # PATH = os.path.abspath(__file__)
    # ROOT = (PATH.split("fnd"))
    # ROOT = ROOT[0] + "fnd/" + "SoundCode/logs"
    # file_name = ROOT + "/log_resposiveness.json"
    # f = open(file_name, "r")
    # # print(f.read())
    #
    # data = f.read()
    # data = data.split("}")
    #
    # arr_to_handle = []
    #
    # for x in data:
    #     try:
    #         dict_i = {}
    #         x = x[2:]
    #         x = x.split(",")
    #         for et in x:
    #             # print(et)
    #             et = et.split(":")
    #             name = et[0]
    #             name = name.replace("\'","")
    #             val = et[1]
    #             val = val.replace("\'", "")
    #             dict_i[name] = val
    #
    #         arr_to_handle.append(dict_i)
    #     except:
    #         print("skip")
    #
    # arr_to_handle_two = []
    # for y in arr_to_handle:
    #     try:
    #         if "<TypeLogs.TESTING" in y[" type"]:
    #             arr_to_handle_two.append(y)
    #     except:
    #         print("skip")
    #
    # for elt in arr_to_handle_two:
    #     print(elt)

    # for z in range(len(arr_to_handle_two)):
    #     time = float(arr_to_handle_two[z+1][' timestamp']) - float(arr_to_handle_two[z][' timestamp'])
    #     print(str(arr_to_handle_two[z][' msg']) ,"time to action ",time)
    #     z = z + 2

    print("*"*100)


    #
    # save_msg_to_cache(text, "tutorial")
    #
    # play_msg_cache("tutorial")

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
