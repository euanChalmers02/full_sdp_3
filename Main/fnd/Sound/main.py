import time

from Sound.SoundSys.TextToSpeech import *

if __name__ == "__main__":
    print("Hello, World!")
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