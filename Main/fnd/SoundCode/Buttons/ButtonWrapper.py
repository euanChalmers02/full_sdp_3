from fnd.SoundCode.SoundSys.TextToSpeech import play_msg_cache

ALL_COMMANDS = []

class ThreadingState:

    # how to refine into one sys variable
    # how to have super states
    def __init__(self):
        print("init")
        self.stop = False
        self.read_out = False
        self.no_beeps = 3
        self.pause_length = 1
        self.quit = False
        self.all_objects = []
        self.voice = False
        self.ocr = False
        self.dist = False
        self.super_state = None

    def str_print(self):
        print('Stop', self.stop)
        print('Read out', self.read_out)
        print('Quit', self.quit)

    # take the letter from the buttons or voice commands e.g. A, B, C
    def commandInterface(self, cmd):
        print("cmd sent is |-> ", cmd)

        # add the commands of the type class
        filtered_arr = [p for p in ALL_COMMANDS if p.state == "any" or p.state == self.super_state]
        for elt in filtered_arr:
            if elt.cmd == cmd:
                play_msg_cache(elt.play)
                state.sysState = elt.set_to
                print("--> state ", elt.state)
            else:
                print("throw error if command not found in this state")


state = ThreadingState()

# a command should either be in an any active state or specified for each which it is available
class Command:
    def __init__(self, state_active, cmd, play, set_to):
        self.state = state_active
        self.cmd = cmd
        self.play = play
        self.set_to = set_to

# New buttons will be bnm
# STATES = ["pause", "voice", "ocr", "scan", "dist"]
# All commands

# pause
ALL_COMMANDS.append(Command("all",'b','pause','pause'))
# resume (should return to historic state of some kind?
ALL_COMMANDS.append(Command("all",'b','pause','scan'))
