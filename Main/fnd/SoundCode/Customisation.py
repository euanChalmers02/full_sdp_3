import json
from os import walk
from Main.fnd.SoundCode.SoundSys.TextToSpeech import *
# from Logging import *
from Main.fnd.SoundCode.SoundSys.VoiceToText import listen

engine = pyttsx3.init()


def change_voice_property(index):
    file = open(CACHE_JSON_FILE)
    data = json.load(file)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[index].id)

    f = []
    for (dirpath, dirnames, filenames) in walk(MSG_CACHE_PATH):
        f.extend(filenames)
        break

    #     How to to know what was said..... create a directory of what is said... (chnage the code)
    for elt in f:
        print(elt)
        save_msg_to_cache(data[elt], elt)

    file.close()


# dummy commands to be added
def update_type_of_beep(ind):
    return


def update_num_beeps(ind):
    return


# logging should moniter the success rate to the file
def select_an_option():
    res = listen()
    if "quit" in res:
        # add_log("VOICE COMMAND,FAIL," + res)
        play_msg_cache('Quitting')
        return None
    else:
        #         could cache this possibly...??
        engine.say('Is ' + res + " correct?")
        engine.runAndWait()

        rez = listen()
        if "yes" in rez:
            # add_log("VOICE COMMAND,Success," + res)
            play_msg_cache('Great_Updating_Now')
            return res
        elif "quit" in rez or "no" in rez:
            # add_log("VOICE COMMAND,FAIL," + res)
            play_msg_cache('Quitting')
            return None
        else:
            # add_log("VOICE COMMAND,FAIL," + res)
            play_msg_cache('say_again')
            select_an_option()


def cycle_voices():
    voices = engine.getProperty('voices')

    for y in range(5):
        engine.setProperty('voice', voices[y].id)
        engine.say('Voice ' + str(y))
        engine.runAndWait()

    play_msg_cache('voice_number_start')

    #     call the selection method
    ind = select_an_option
    if ind is not None:
        change_voice_property(ind)


def cycle_beeps():
    #    need to change once in main program
    PATH = os.path.abspath(__file__)
    ROOT = (PATH.split("fnd"))
    mypath = ROOT[0] + "fnd/beeps"
    print(mypath)

    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break

    print(f)
    engine = pyttsx3.init()

    for idx, each in enumerate(f):
        if '.wav' in each:
            engine.say('Beep ' + str(idx + 1))
            engine.runAndWait()

            file_name = mypath + '/' + each

            [y, sr] = librosa.load(file_name, sr=48000)
            duration = librosa.get_duration(filename=file_name) * 1000  # value in ms

            sd.play(y, sr)
            sd.sleep(int(duration))
            sd.stop()

    play_msg_cache('beep_type_start')

    ind = select_an_option()
    if ind is not None:
        update_type_of_beep(ind)


def customise_number_beeps():
    play_msg_cache('customise_beeps_start')
    #     how to speed up the wait here

    ind = select_an_option()
    if ind is not None:
        update_num_beeps(ind)
