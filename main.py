import win32api, win32con
import pyautogui
import time
import sys
import pyscreenshot as ImageGrab
import pytesseract
import argparse

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
def capture(screenshots, filename):
    myScreenshot = pyautogui.screenshot()
    try:
        myScreenshot.save(r"../"+screenshots+"\\"+filename+".png")
    except ValueError as ve:
        print(filename)
        print(ve)
        print("../"+screenshots+"\\"+filename+".png")

def capture_testanswers(nbQuestions):
    for i in range(nbQuestions):
      #on vclique maintenant sur la fleche suivante plutot que sur les questions
      click(1850+xoffset,650+yoffset)
      #sleep pour laisser à la page web de se charger
      time.sleep(.5)
      #cette ligne est pour la web version plein ecran sur chrome
      im=ImageGrab.grab(bbox=(1650,300,1802,360))
      im.save('../tmp/'+str(i)+'.png')
      pytesseract.pytesseract.tesseract_cmd = r'..\tesseract-OCR\tesseract.exe'
      text_image = pytesseract.image_to_string(r'../tmp\\'+str(i)+'.png')
      print(text_image)
      reference = (extract_reference_from_textimage(text_image))
      print(reference)
      capture("screenshots", reference)
      
def can_convert_to_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def extract_reference_from_textimage(string):
    reference = ""
    for s in string:
        if can_convert_to_int(s):
            reference = reference + s
        if s == "S":
            break
    return reference

number_of_questions = 0
xoffset = 0
yoffset = 0

parser = argparse.ArgumentParser(description='Help menu')
parser.add_argument('--xoffset', dest='xoffset', type=str, help='X offset (default 0), usefull for tests with more 26 questions')
parser.add_argument('--yoffset', dest='yoffset', type=str, help='Y offset (default 0), usefull for BGS web version or other screen configuration')
parser.add_argument('--questions', dest='questions', type=int, help='number of questions to iterate')

args = parser.parse_args()

if args.xoffset:
    xoffset = int(args.xoffset)
if args.yoffset:
    yoffset = int(args.yoffset)
if args.questions:
    number_of_questions = int(args.questions)

capture_testanswers(number_of_questions)
    

print("May the force be with you young pilot!")