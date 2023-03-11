import sys
import time
import sounddevice as sd
import threading

from Main.fnd.SoundCode.Logging import add_log
from Main.fnd.SoundCode.SoundSys.TextToSpeech import play_msg_cache
from Main.fnd.SoundCode.Customisation import *


# method to loop through states??? where to put and why....
def next_mode(curr):
    # STATES = [{"pause":"pause"}, {"voice":""}, {"Scan+ocr":"ocr"}, {"Scan":"resuming_scan"}, {"dist":"dist"},{"customise":""}]
    STATES = [{"Scan+ocr": "ocr"}, {"Scan": "Scan_Mode"},{"dist": "dist"}]
    for y in range(len(STATES)):
        if list(STATES[y].keys())[0] == curr:
            index = y+1
            if index >= len(STATES):
                # play_msg_cache(list(STATES[0].values())[0])
                print("mode -> ",list(STATES[0].keys())[0])
                return list(STATES[0].keys())[0]
            else:
                # play_msg_cache(list(STATES[y+1].values())[0])
                print("mode ->",list(STATES[y+1].keys())[0])
                return list(STATES[y+1].keys())[0]


def get_audio(ste):
    STATES = [{"Scan+ocr": "ocr"}, {"Scan": "Scan_Mode"},{"dist": "dist"}]
    for y in range(len(STATES)):
        if list(STATES[y].keys())[0] == ste:
            return list(STATES[y].values())[0]

# a command should either be in an any active state or specified for each which it is available
class Command:

    def __init__(self, state_active, cmd, play, set_to, execute=None):
        self.state = state_active
        self.cmd = cmd
        self.play = play
        self.set_to = set_to
        self.execute = execute

    def pretty_print_command(self):
        print("*" * 15)
        print(f"Command: \n"
              f"    *Can be called within... {self.state} \n"
              f"    *Is called by... {self.cmd}  \n"
              f"    *Play... {self.play}  \n"
              f"    *Sets sysState to... {self.set_to}")
        print("*" * 15)


# New buttons will be bnm
# All commands
ALL_COMMANDS = []
# pause
ALL_COMMANDS.append(Command("all", 'AA', 'pause', 'pause'))
# resume (should return to historic state of some kind? (return to history state)
ALL_COMMANDS.append(Command("all", 'AA', 'resuming_scan', 'Scan'))  # should in future be set to historic state

ALL_COMMANDS.append(Command("Scan", 'A', '','', next_mode))
ALL_COMMANDS.append(Command("Scan+ocr", 'A', '','', next_mode))
ALL_COMMANDS.append(Command("dist", 'A', '','', next_mode))

# volume up
ALL_COMMANDS.append(Command("all", 'B', '', '', audio_driver_up))
# volume down
ALL_COMMANDS.append(Command("all", 'C', '', '', audio_driver_down))


# print("ALL COMMANDS = ",ALL_COMMANDS)


class ThreadingState:

    def __init__(self):
        self.no_beeps = 3
        self.pause_length = 1
        self.all_objects = []
        self.sysState = "Scan"
        self.id = time.time()
        self.debug = False

        self.ALL_COMMANDS = ALL_COMMANDS
        self.sysPlatfrom = sys.platform
        self.histState = None
        self.lock = threading.Lock()
        # used to resume from pause (not currently needed due to pause command)
        # self.historicSysState = ""

    # take the letter from the buttons or voice commands e.g. A, B, C
    def commandInterface(self, cmd):
        print("cmd sent is |-> ", cmd)

        # placeholder catch for pause state checking (all states , bypassess command structure for now)

        if cmd == 'AA':
            if self.sysState == "pause":
                # change to resume mode
                self.lock.acquire()
                play_msg_cache("resuming_scan")
                self.lock.release()
                self.sysState = self.histState
            else:
                self.histState = self.sysState
                self.lock.acquire()
                play_msg_cache('pause')
                self.lock.release()
                self.sysState = "pause"
            return True
        else:
            # add the commands of the type class
            filtered_arr = [p for p in self.ALL_COMMANDS if p.state == "all" or p.state == self.sysState]
            for elt in filtered_arr:
                if elt.cmd == cmd:
                    self.histState = self.sysState
                    # should be no change to sys state in imitate commamnds
                    if elt.execute is not None:
                        print("else triggered")
                        xr = elt.execute

                        # for next mode button
                        if xr == next_mode:
                            print("current state of dist thread is...",)
                            d = xr(self.sysState)

                            # so nothing else can happen??
                            self.lock.acquire()
                            play_msg_cache(get_audio(d))
                            self.lock.release()

                            # self.play_snd_wrapper(d)
                            self.sysState = d
                        else:
                            # for things like volume up/down/customise options
                            xr()
                        add_log("activity log->"+str(self.sysState))
                        return True
                    else:
                        # for nomal buttons
                        self.sysState = elt.set_to
                        self.lock.acquire()
                        play_msg_cache(elt.play)
                        self.lock.release()
                        print(self.id, "<->state ", self.sysState)
                        add_log("activity log->"+self.sysState)
                        return True

            print("INVALID COMMAND -> throw error")
            add_log("activity log->"+self.sysState)
            return False

    def get_state(self):
        return self.sysState

    def set_state(self, cnd):
        self.sysState = cnd

    def add_command(self, Command):
        self.ALL_COMMANDS.append(Command)
        return True

    # def play_snd_wrapper(self,o):
    #     while self.threadX.is_alive():
    #         time.sleep(0.00000000005)

        # play_msg_cache(get_audio(o))



