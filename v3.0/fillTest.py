import pngFinderFromFillTest
import pyscreenshot as ImageGrab
import pytesseract
import argparse


def find_answer(directory):
    #semble marcher sur tout les tests un peu moins precise donc demande un peu de traitement pour recuperer la reference
    #im=ImageGrab.grab(bbox=(1600,300,1752,420))
    #la suivante est plus précise mais sur certain tests ne marche pas
    #im=ImageGrab.grab(bbox=(1600,300,1752,390))
    im=ImageGrab.grab(bbox=(1600,100,1800,250))
    im.save('../tmp/1.png')
    pytesseract.pytesseract.tesseract_cmd = r'..\tesseract-OCR\tesseract.exe'
    text_image = pytesseract.image_to_string(r'../tmp\\1.png')
    print(text_image)
    reference = (extract_reference_from_textimage(text_image))
    #print(reference)
    #f = open("../demofile2.txt", "a")
    #f.write(pytesseract.image_to_string(r'../tmp\\'+str(i)+'.png'))
    #f.close()
    #quit()
    pngFinderFromFillTest.find_ref(reference, directory)
  
def extract_reference_from_textimage(string):
    reference = ""
    for s in string:
        if can_convert_to_int(s):
            reference = reference + s
        if s == "S":
            break
    return reference
    
def can_convert_to_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
      
      
      
      
#pngFinder
parser = argparse.ArgumentParser(description='Help menu')
parser.add_argument('--dir', dest='dir', type=str, help='directory to find reference in')
args = parser.parse_args()
directory = ""
if args.dir:
    directory = args.dir
    
find_answer(directory)