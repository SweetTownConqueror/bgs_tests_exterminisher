import win32api, win32con
import pyautogui
import time
import sys

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
def capture(screenshots, filename):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"../"+screenshots+"\\"+filename+".png")

def answer_test(nbQuestions):
    z=0
    for i in range(nbQuestions):
      click(176+z,291)
      time.sleep(1)
      click(330,646)
      #time.sleep(1)
      z=z+62

def capture_testanswers(nbQuestions):
    z=0
    for i in range(nbQuestions):
      click(176+z,291)
      time.sleep(0.5)
      capture("screenshots", str(i))
      z=z+62
      
def can_convert_to_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


#capture("screenshot", "a")
#pour 26 questions mettrre 29
#answer_test(29)

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
  #print(type(args))
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

  
#capture_testanswers(29)
print("Hello")
print("World")