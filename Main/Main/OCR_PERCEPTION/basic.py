import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd= '/usr/local/Cellar/tesseract'
from Main.fnd.SoundCode.SoundSys.OCR import *

PATH = os.path.abspath(__file__)
ROOT = PATH.split("Main")
PATH = ROOT[0] + "Main/SoundCode/logs/"

def get_text(img):
    return pytesseract.image_to_string(img)

def image_to_text(img):
    # pytesseract
    # image_path = "/Users/euanchalmers/Desktop/ocr/imges/ocrtest_shift.png"
    # image = cv2.imread(image_path)

    text = get_text(img)
    # print(text)
    # this will create the text object and should play the identified text (allowing for pauses etc)
    OCR(text)
    # print("Complete ocr func")

    # log the img (for us to analyse in future)
    if text != "":
        from numpy import random
        code = random.randint(100)
        cv2.imwrite(PATH+code+'.jpg', img)
        add_log("OCR-",code,"-",text)