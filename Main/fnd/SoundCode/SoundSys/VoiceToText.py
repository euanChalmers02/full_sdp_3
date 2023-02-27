import speech_recognition as sr
from Main.fnd.Sound.SoundSys.TextToSpeech import *

# on button press start listening and return command
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        r.energy_threshold = 4000
        try:
            audio = r.listen(source, 2)  # Starts Listening
        except:
            print("Sorry, couldn't hear you!")
            return None
    try:
        text = r.recognize_google(audio)  # Recognizes audio in English
        return (text)

    except:  # When there is no notable speech
        print("Sorry, couldn't hear you!")
        return None


COMMANDS = ["pause", "resume", "stop", "read out full", "customise beep sound", "customise voice",
            "customise number of beeps"]
COMMANDS_BUTTONS = {"pause": "p", "resume": "r", "stop": "s", "read out full": "m", "customise beep sound": "bs",
                    "customise voice": "cv", "customise number of beeps": "cnb"}


def parse(voice_command):
    print(voice_command)
    for o in COMMANDS:
        if o in voice_command:
            print("Command said is ... ", o)
            return COMMANDS_BUTTONS[o]


# call when the voice command is called
def voice_wrapper():
    res = listen()

    if res is None:
        play_msg_cache('default')
        return None
    else:
        return parse(res)

