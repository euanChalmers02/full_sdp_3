import json
from os import walk
from Main.fnd.SoundCode.SoundSys.TextToSpeech import *
import speech_recognition as sr
import os
import sys

# TODO: change if on Pi
os_plat = sys.platform

if os_plat == "darwin":
    os_plat = "mac"
else:
    os_plat = "pi"

# from Logging import *

# engine = pyttsx3.init()

# on button press start listening and return command
def cus_listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        r.energy_threshold = 4000
        try:
            audio = r.listen(source, 2)  # Starts Listening
        except:
            print("Sorry")
            return None
    try:
        text = r.recognize_google(audio)  # Recognizes audio in English
        return text

    except:  # When there is no notable speech
        print("Sorry, couldn't hear you!")
        return None


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
    res = cus_listen()
    if "quit" in res:
        # add_log("VOICE COMMAND,FAIL," + res)
        play_msg_cache('Quitting')
        return None
    else:
        #         could cache this possibly...??
        engine.say('Is ' + res + " correct?")
        engine.runAndWait()

        rez = cus_listen()
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


def get_audio_level(os_plat):
    if os_plat == "mac":
        stream = os.popen("osascript -e 'get volume settings'")
        output = stream.read()
        output = output.split(":")[1]
        return output.split(',')[0]

    elif os_plat == "pi":
        stream = os.popen("amixer get Master")
        output = stream.read()
        print(output)
    else:
        print("unknown os")


""" ---- FOR MAC ----- 
    osascript -e'set volume "<<VALUE>>"'

    <<VALUE>> | actual system volume percentage
        0     |     0
        1     |     14
        2     |     29
        3     |     43
        4     |     57
        5     |     71
        6     |     86
        7     |     100
"""


def update_level_to(os_plat, level):
    if os_plat == "mac":
        stream = os.popen("osascript -e'set volume " + str(level) + "' ")
        output = stream.read()
        print(output)
    elif os_plat == "pi":
        stream = os.popen("amixer set Master " + str(level) + "%")
        output = stream.read()
        print(output)
    else:
        print("unknown os")


def audio_driver_up():

    if os_plat == "pi":
        curr = get_audio_level(os_plat)
        print("audio level", curr)

        level = int(curr) + 10

        # check limit
        if level < 0:
            level = 0
        elif level > 100:
            level = 100

        print("level = ", level)
        update_level_to(os_plat, level)

    elif os_plat == "mac":
        curr = get_audio_level(os_plat)
        print("audio level", curr)

        level = (int(curr) + 15) // 14

        # check limit
        if level < 0:
            level = 0
        elif level > 100:
            level = 100

        print("level = ", level)
        update_level_to(os_plat, level)


def audio_driver_down():
    if os_plat == "pi":
        curr = get_audio_level(os_plat)
        print("audio level", curr)

        level = int(curr) - 10

        # check limit
        if level < 0:
            level = 0
        elif level > 100:
            level = 100

        print("level = ", level)
        update_level_to(os_plat, level)

    elif os_plat == "mac":
        curr = get_audio_level(os_plat)
        print("audio level", curr)

        level = (int(curr) - 15) // 14

        # check limit
        if level < 0:
            level = 0
        elif level > 100:
            level = 100

        print("level = ", level)
        update_level_to(os_plat, level)