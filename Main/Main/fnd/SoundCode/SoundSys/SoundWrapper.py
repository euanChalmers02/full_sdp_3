import pyttsx3

from Main.fnd.SoundCode.SoundSys.TextToSpeech import play_msg_cache
from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
state = get_instate_of_state()
from Main.fnd.SoundCode.Buttons.ButtionChange import *


# -- customisable --
# move this to a sound wrapper
pause_length = 3
no_beeps = 3


def sound_action(snd):
    # add the command logic here if the multithreading works
    # check for if pause while beeping
    if state.get_state() == "Scan":
        o = snd
        print(o.get_name())
        print(o)

        play_msg_cache(o.get_name())
        o.create_3d()

        if state.get_state() == "Scan":
            for _ in range(no_beeps):
                o.play()
            time.sleep(pause_length)
        else:
            func = check_next_func()
            func()
    else:
        func = check_next_func()
        func()
