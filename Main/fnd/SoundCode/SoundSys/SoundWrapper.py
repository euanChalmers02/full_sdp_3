import pyttsx3

from Main.fnd.SoundCode.Buttons.ButtonActions import *
from Main.fnd.SoundCode.SoundSys.TextToSpeech import play_msg_cache
from Main.fnd.SoundCode.Buttons.ButtonWrapper import *

# -- customisable --
# move this to a sound wrapper
pause_length = 3
no_beeps = 3


def sound_action(snd):
    # add the command logic here if the multithreading works
    print('button status', check_next_func())

    # check for if pause while beeping
    if check_next_func() is None:
        o = snd
        print(o.get_name())
        print(o)

        play_msg_cache(o.get_name())
        o.create_3d()

        if check_next_func() is None:
            for _ in range(no_beeps):
                o.play()
            time.sleep(pause_length)
        else:
            func = check_next_func()
            func()
    elif check_next_func() == quit_action:
        quit_action()
        return
    else:
        func = check_next_func()
        func()
