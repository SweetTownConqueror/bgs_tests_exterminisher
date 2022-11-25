import win32api, win32con
import pyautogui
import time
import sys
import pyscreenshot as ImageGrab
import pytesseract

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

def answer_test(nbQuestions):
    z=0
    for i in range(nbQuestions):
      click(176+z,291)
      time.sleep(1)
      click(330,646)
      #time.sleep(1)
      z=z+pas

def capture_testanswers(nbQuestions):
    z=0
    for i in range(nbQuestions):
      #click(225+z,291)
      click(176+z,291)
      time.sleep(0.5)
      #trouver la reference pour la passer en nom de capture à la fonction capture
      #im=ImageGrab.grab(bbox=(1625,360,1755,440))
      #im=ImageGrab.grab(bbox=(1625,370,1755,420))
      #semble marcher sur tout les tests un peu moins precise donc demande un peu de traitement pour recuperer la reference
      im=ImageGrab.grab(bbox=(1600,300,1752,420))
      #la suivante est plus précise mais sur certain tests ne marche pas
      #im=ImageGrab.grab(bbox=(1600,300,1752,390))
      im=ImageGrab.grab(bbox=(1600,350,1752,420))
      im.save('../tmp/'+str(i)+'.png')
      pytesseract.pytesseract.tesseract_cmd = r'..\tesseract-OCR\tesseract.exe'
      text_image = pytesseract.image_to_string(r'../tmp\\'+str(i)+'.png')
      print(text_image)
      reference = (extract_reference_from_textimage(text_image))
      print(reference)
      #f = open("../demofile2.txt", "a")
      #f.write(pytesseract.image_to_string(r'../tmp\\'+str(i)+'.png'))
      #f.close()
      #quit()
      capture("screenshots", reference)
      z=z+pas
      
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
    
print("Pass the action you want to as argument and the number of question to answer")
print("ex: -parse 26 or -screen 10")

pas=61
invalid_argument = True
function_parse = False
function_screen = False
number_of_questions = 0
for args in sys.argv:

  if args == "-parse":
    invalid_argument = False
    function_parse = True
  if args == "-screen":
    invalid_argument = False
    function_screen = True
  if can_convert_to_int(args):
    number_of_questions = int(args)
    
if invalid_argument == True:
    print("Invalid argumment entered.")
    print("argument: -parse to parse bgs test")
    print("argument: -screen to screen bgs test")
    print("add number of questions")
    print("example : python main.py -parse 26")

if function_parse == True:
    answer_test(number_of_questions)
if function_screen == True:
    capture_testanswers(number_of_questions)

print("May the force be with you young pilot!")