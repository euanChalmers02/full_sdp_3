import pyttsx3

# -- customisable --
# move this to a sound wrapper
pause_length = 3
no_beeps = 3

from fnd.SoundCode.ButtonWrapper import *


# current array clean will not let the same object be registered twice in 2 seconds
def clean_arr(curr, arr_snds):
    # TODO: ?
    return


def sound_action(snd, arr_sounds):
    print('the current array length is ', len(arr_sounds))
    # add the command logic here if the multithreading works
    print('button status', check_next_func())
    update_object(snd)

    # check for if pause while beeping
    if check_next_func() is None:
        o = snd
        print(o.get_name())
        print(o)

        play_msg_cache(o.get_name())
        o.create_3d()
        # o.textToSpeech()
        for _ in range(no_beeps):
            o.play()
        time.sleep(pause_length)
    elif check_next_func() == quit_action:
        quit_action()
        return
    else:
        func = check_next_func()
        func()
