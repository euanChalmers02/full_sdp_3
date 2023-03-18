# from Main.PinTesting import check_system
from Main.Main.fnd.SoundCode.Buttons.sysState import ThreadingState

instance = None
state = ""

# this should ensure it is only created once (is a fake ish singleton)
def get_instate_of_state():
    global instance
    global state

    if instance is None:
        # check_system()
        print("new init called")
        state = ThreadingState()
        instance = True
        return state
    else:
        return state