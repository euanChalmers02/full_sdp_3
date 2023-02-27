import time
import os

PATH = os.path.abspath(__file__)
ROOT = (PATH.split("fnd"))
ROOT = ROOT[0] + "fnd/" + "SoundCode/logs"

LOG_FILES = os.listdir(ROOT)
num_of_log_files = (len(LOG_FILES))

ALL_LOGS = []
file_name = 'log_file_' + str(num_of_log_files+1)

def add_log(msg):
    Log(msg)

def save_logs_to_file():
    f = open(ROOT+"/"+file_name + ".json", "w")
    f.write(str(ALL_LOGS))
    print('saved file')
    f.close()


class Log:
    def __init__(self, msg):
        self.timestamp = time.time()
        self.msg = msg
        self.num = len(ALL_LOGS) + 1
        self.dict_item = {"num": self.num, "msg": self.msg, "timestamp": self.timestamp}

        ALL_LOGS.append(self.dict_item)

    def get_item(self):
        print(self.dict_item)
