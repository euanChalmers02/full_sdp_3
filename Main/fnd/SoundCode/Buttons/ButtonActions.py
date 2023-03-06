import time
from Main.fnd.SoundCode.Buttons.ButtonWrapper import state
from Main.fnd.SoundCode.SoundSys.VoiceToText import voice_wrapper_action

def pause_wait_action():
    while check_next_func() is pause_wait_action:
        time.sleep(1)

    print('--> Resume scan')


def read_out_full_action():
    print('--> Reading out full info for ... ', state.current_object.get_name())
    state.current_object.read_full_length()
    state.read_out = False
    time.sleep(0.8)


def quit_action():
    print('nows need to add the quit stuff')
    # play_msg_cache('quit_scanning')

def check_next_func():
    if state.stop:
        return pause_wait_action
    elif state.read_out:
        return read_out_full_action
    elif state.quit:
        return quit_action
    elif state.voice:
        return voice_wrapper_action
    else:
        return None
