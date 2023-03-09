import time
import os
import json
import sys

PATH = os.path.abspath(__file__)
ROOT = (PATH.split("fnd"))
ROOT = ROOT[0] + "fnd/" + "SoundCode/logs"

file_name = ROOT+"/log_all.json"

machine = os.path.abspath(__file__)
machine = machine.split("/")
machine = machine[0] +"-"+ machine[1]+"-"+ machine[2]+"-"+str(sys.platform)

All_logs = []
start_time = time.time()

def add_log(msg):
    Log(msg)


def save_logs_to_file():
    f = open(file_name, "r")
    # print(file_name)
    data = json.load(f)
    f.close()


    data_new = data + All_logs
    with open(file_name, 'w') as f:
        json.dump(data_new, f)

    print('saved file')


class Log:
    def __init__(self, msg):
        self.timestamp = time.time()
        self.msg = msg
        self.num = str(round(start_time))+"_"+str(len(All_logs) + 1)
        # need to change the run num here
        self.dict_item = {"num": self.num, "msg": self.msg, "timestamp": self.timestamp,"machine":machine}

        All_logs.append(self.dict_item)

    def get_item(self):
        print(self.dict_item)
