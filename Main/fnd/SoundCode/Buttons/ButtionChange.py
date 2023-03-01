import queue

from Main.fnd.SoundCode.SoundSys.TextToSpeech import *
from Main.fnd.SoundCode.Buttons.ButtonWrapper import state
from Main.fnd.SoundCode.Logging import *

# possibly an enum
# this should hold the current sys state that can be easly checked
curr_action_status = None


# this is where the buttons to command transfer will happen / including all the gpi port work
def console():
    flag = True
    print('thread started')
    while flag:
        cmd = input('>')
        cmd_queue.put(cmd)
        action = BUTTONS_TO_COMMANDS.get(cmd, invalid_input)
        print("action ",action)
        action()
        print('the curr state ', state.str_print())


# Calling
def invalid_input():
    print('---> Unknown command')


def voice():
    state.voice = True


def pause():
    # how to check if the variable is met throughout the operation??? or is there a better way to kill a thread
    state.stop = True
    play_msg_cache('pause')
    # add the voice recording from TextToSpeechHere
    print('--> Pause action & kill thread')
    # saves all the logs on pause
    save_logs_to_file()



# how to pause somthing
def resume():
    state.stop = False
    play_msg_cache('resuming_scan')



def quit():
    state.quit = True
    print('---> Stop scanning mode')



# this should be in sound development
def read_out_full():
    state.read_out = True
    print('--> Read action called and waiting to activate')
    return


# these are the mappings of the buttons to actions
cmd_queue = queue.Queue()
BUTTONS_TO_COMMANDS = {'p': pause, 'm': read_out_full, 'r': resume, 'q': quit, 'v': voice}

