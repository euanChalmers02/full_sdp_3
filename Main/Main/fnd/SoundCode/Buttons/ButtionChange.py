from Main.fnd.SoundCode.SoundSys.VoiceToText import voice_wrapper_action
from Main.fnd.SoundCode.SoundSys.DIST import distance_action_or_state
from Main.fnd.SoundCode.Logging import *
from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
# import RPi.GPIO as GPIO
import time

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


# used for testing buttons can be thrown
def button_thows():
    list_of_commands_to_send = ["AA","A","A","A","A","B","B","B","C"]
    sleep_time = 1
    time.sleep(4)
    print('buttons throwing sys')

    for x in range(len(list_of_commands_to_send)):
        cmd = list_of_commands_to_send[x]
        state.commandInterface(cmd)
        time.sleep(sleep_time)


def pause_wait_action():
    save_logs_to_file()
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