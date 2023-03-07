import time

from Main.fnd.SoundCode.SoundSys.VoiceToText import voice_wrapper_action
from fnd.SoundCode.SoundSys.DIST import distance_action_or_state
from Main.fnd.SoundCode.Logging import *
from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
state = get_instate_of_state()

def console_two():
    flag = True
    print('thread started')
    while flag:
        try:
            cmd = input('>')
            state.commandInterface(cmd)
        except EOFError as e:
            print(e)

# def exit_mode():
#     state.ocr = False
#     state.dist = False

def pause_wait_action():
    while state.get_state() == "pause":
        time.sleep(1)

    print('--> Resume scan')


def check_next_func():
    next_func = {"pause": pause_wait_action, "dist": distance_action_or_state, "voice": voice_wrapper_action}
    act = next_func[state.get_state()]
    if act is not None:
        return act
    else:
        print("could not find next command")
        return None