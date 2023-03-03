import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

PATH = os.path.abspath(__file__)
print(PATH)
# ROOT = PATH.split("Main")
# PATH = ROOT[0] + "Main/recorded_msg"

def image_to_text():
    # pytesseract
    image_path = "/Users/euanchalmers/Desktop/ocr/imges/ocrtest_shift.png"
    image = cv2.imread(image_path)

    text = pytesseract.image_to_string(image)
    print(text)