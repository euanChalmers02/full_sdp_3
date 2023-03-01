import speech_recognition as sr
from Main.fnd.SoundCode.SoundSys.TextToSpeech import *
from Main.fnd.SoundCode.Buttons.ButtonWrapper import *
from Main.fnd.SoundCode.Buttons.ButtionChange import *
from Main.fnd.SoundCode.Customisation import *

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
        return text

    except:  # When there is no notable speech
        print("Sorry, couldn't hear you!")
        return None

# this should allow for multiple phrases to be passed and point to same 'button'
COMMANDS_BUTTONS = {"pause": pause, "resume": resume, "stop": quit, "read out full": read_out_full, "customise beep sound": cycle_beeps,
                    "customise voice": cycle_voices , "customise number of beeps" : customise_number_beeps}

def parse(voice_command):
    print(voice_command)
    for o in COMMANDS_BUTTONS.keys():
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

def voice_wrapper_action():
    state.voice = False
    play_msg_cache('Speak_now')
    res = listen()

    if res is None:
        print("default msg said")
        play_msg_cache('default')
        return None
    else:
        result = parse(res)
        #should run the state change similar to the buttons
        result()
        print("Called " + str(result) + " from VoiceToText!")
        return True


