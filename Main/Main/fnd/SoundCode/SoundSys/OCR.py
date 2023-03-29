# OCR commands to read out full text??
import pyttsx3
from Main.fnd.SoundCode.Buttons.ButtionChange import *
from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state
state = get_instate_of_state()


class OCR:

    # should kill in multithreading if state changed using the onword?
    def onWord(self,name, location, length):

        self.word_num = self.word_num + 1
        if state.get_state() != "ocr":
            action = check_next_func()
            self.engine.stop()
            action()
            print("break @ ", self.word_num)
            self.textToSpeech()
            print("this should resume?")
            # print("should now resume engine @the last word said & engine should be deid ",self.engine.isBusy())

    # def onEnd(self,name, completed):
    #     # self.engine.stop()
    #     print('finish callback ', name, completed)

    def textToSpeech(self):

        # self.engine = pyttsx3.init()

        if self.text == "":
            return

        #

        engine = pyttsx3.init()
        engine.say(self.text)
        engine.runAndWait()
        print("finsihed")


        return True

    def __init__(self, text):
        self.engine = pyttsx3.init()
        self.text = text
        self.word_num = 0

        self.textToSpeech()


