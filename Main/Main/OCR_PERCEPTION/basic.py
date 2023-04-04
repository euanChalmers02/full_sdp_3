import pytesseract
import cv2
import os
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
from Main.fnd.SoundCode.SoundSys.OCR import *

PATH = os.path.abspath(__file__)
ROOT = PATH.split("Main")
PATH = ROOT[0] + "Main/SoundCode/logs/"

def image_to_text(img):
    # pytesseract
    # image_path = "/Users/euanchalmers/Desktop/ocr/imges/ocrtest_shift.png"
    # image = cv2.imread(image_path)

    text = pytesseract.image_to_string(img)


    if len(text) >2:
        print(text)
    # this will create the text object and should play the identified text (allowing for pauses etc)
    OCR(text)
    # print("Complete ocr func")
