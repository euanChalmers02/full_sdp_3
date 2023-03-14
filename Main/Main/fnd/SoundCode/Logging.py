import time
import os
import json
import sys
from enum import Enum


class TypeLogs(Enum):
    # change number to reflect serverty for the QA analysis
    ACTIVITY = 1
    VOICE = 1
    GENERAL = 1
    OCR = 1
    THREADING = 1


PATH = os.path.abspath(__file__)
ROOT = (PATH.split("fnd"))
ROOT = ROOT[0] + "fnd/" + "SoundCode/logs"

file_name = ROOT + "/log_all.json"

machine = os.path.abspath(__file__)
machine = machine.split("/")
machine = machine[0] + "-" + machine[1] + "-" + machine[2] + "-" + str(sys.platform)

All_logs = []
start_time = time.time()


def add_log(msg, type=TypeLogs.GENERAL):
    Log(msg, type)


def save_logs_to_file():
    try:
        f = open(file_name, "r")
        # print(file_name)
        data = json.load(f)
        f.close()

        data_new = data + All_logs
        with open(file_name, 'w') as f:
            json.dump(data_new, f)

        print('saved file')
    except:
        print("no files to save")


from numpy import random


class Log:
    def __init__(self, msg, type):
        self.timestamp = time.time()
        self.msg = msg
        self.num = str(round(start_time)) + "_" + str(len(All_logs) + 1)
        self.type = type
        self.run = random.randint(1000000)
        # need to change the run num here
        self.dict_item = {"num": str(self.run) + "_" + self.num, "msg": self.msg, "timestamp": self.timestamp,
                          "machine": machine, "type": self.type}

        All_logs.append(self.dict_item)

    def get_item(self):
        print(self.dict_item)


def get_all_logs():
    print(All_logs)
