import time
import os
import json
import sys
from enum import Enum
from numpy import random


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


def add_log(msg, typeArg=TypeLogs.GENERAL):
    Log(msg, typeArg)


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


def linting():
    print("started")
    import os
    stream = os.popen(
        "flake8 --extend-ignore E275,E501,E225 /Users/euanchalmers/Desktop/full_sdp_3/Main/Main/fnd/SoundCode")
    output = stream.read()
    output = output.split("\n")

    arr_all = []

    PATH_local = os.path.abspath(__file__)
    ROOT_local = (PATH.split("Main"))[0] + "Main/Main/fnd/SoundCode/logs"
    file_name = ROOT + "/linting.json"
    f = open(file_name, "r")
    data = json.load(f)
    f.close()
    vrl = len(data)
    previous = data[vrl - 1]["id"]
    id_r = previous + 1

    for y in range(len(output)):
        try:
            first = output[y].split(":")[0]
            second = output[y].split("[")[1]
            code = second.split("]")[0]
            code = code.strip("[")
            third = second.split("]")[1]

            dict_temp = {"id": id_r, "file": first, "code": code, "error": third}
            arr_all.append(dict_temp)
        except:
            print("misss")

    print(arr_all)
    # saves to the file in the repo hopefully
    new_data = data + arr_all

    with open(file_name, 'w+') as f:
        json.dump(new_data, f)

    print('saved file')


if __name__ == '__main__':
    linting()
