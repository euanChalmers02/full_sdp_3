import time

from fnd.SoundCode.SoundSys.TextToSpeech import play_msg_cache


# a command should either be in an any active state or specified for each which it is available
class Command:
    def __init__(self, state_active, cmd, play, set_to):
        self.state = state_active
        self.cmd = cmd
        self.play = play
        self.set_to = set_to

    def pretty_print_command(self):
        print("*"*15)
        print(f"Command: \n"
              f"    *Can be called within... {self.state} \n"
              f"    *Is called by... {self.cmd}  \n"
              f"    *Play... {self.play}  \n"
              f"    *Sets sysState to... {self.set_to}")
        print("*"*15)


# test
xr = Command("all", 'p', 'pause', 'pause')
xr.pretty_print_command()


# New buttons will be bnm
# All commands
ALL_COMMANDS = []
# pause
ALL_COMMANDS.append(Command("all", 'p', 'pause', 'pause'))
# resume (should return to historic state of some kind?
ALL_COMMANDS.append(Command("all", 'r', 'resuming_scan', 'Scan')) #should in future be set to historic state
# ocr (note this must contain the words "scan" and "ocr"
ALL_COMMANDS.append(Command("all", 'o', 'ocr', 'Scan+ocr'))
# dist
ALL_COMMANDS.append(Command("all", 'd', 'dist', 'dist'))
# voice
ALL_COMMANDS.append(Command("all", 'v', '', 'voice'))
# scan mode (should be deprecated)
ALL_COMMANDS.append(Command("all", 's', 'resuming_scan', 'Scan'))

# print("ALL COMMANDS = ",ALL_COMMANDS)


class ThreadingState:

    # how to refine into one sys variable
    # how to have super states
    # STATES = ["pause", "voice", "ocr", "scan", "dist","customise"]
    def __init__(self):
        self.no_beeps = 3
        self.pause_length = 1
        self.all_objects = []
        self.sysState = "Scan"
        self.id = time.time()
        self.debug = False
        self.ALL_COMMANDS = ALL_COMMANDS
        # used to resume from pause (not currently needed due to pause command)
        # self.historicSysState = ""

    # take the letter from the buttons or voice commands e.g. A, B, C
    def commandInterface(self, cmd):
        print("cmd sent is |-> ", cmd)

        # add the commands of the type class
        filtered_arr = [p for p in self.ALL_COMMANDS if p.state == "all" or p.state == self.sysState]
        for elt in filtered_arr:
            if elt.cmd == cmd:
                play_msg_cache(elt.play)
                self.sysState = elt.set_to
                print(self.id,"<->state ", self.sysState)
                return True

        print("INVALID COMMAND -> throw error")
        return False

    def get_state(self):
        return self.sysState

    def set_state(self,cnd):
        self.sysState = cnd

    def add_command(self,Command):
        self.ALL_COMMANDS.append(Command)
        return True
