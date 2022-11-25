from os import walk
from PIL import Image
import sys
import argparse

print("Pass your destination folder as argument to search to specific folder (default: screenshots)")
print("q: quit")

search_directory = "./screenshots"
parser = argparse.ArgumentParser(description='Help menu')
parser.add_argument('--dir', dest='dir', type=str, help='directory into which find references')
parser.add_argument('--fromAnotherScript', dest='fromAnotherScript', type=str, help='Allows a different execution if the script is run form another script')
parser.add_argument('--ref', dest='ref', type=str, help='If the script is run form another script search for reference')

args = parser.parse_args()
if args.fromAnotherScript:
    if args.dir:
        search_directory = args.dir
    if args.ref:
        reference = args.ref+".png"
    listeFichiers = []
    for (repertoire, sousRepertoires, fichiers) in walk("../"+search_directory):
        listeFichiers.extend(fichiers)
    #print(listeFichiers)
    if reference in listeFichiers:
        print("found!")
        print(reference)
        img = Image.open("../"+search_directory+"/"+reference)
        img.show()
    else:
        print("not found!")
else:
    if args.dir:
        search_directory = args.dir
        
    prompt = ""
    while prompt != "q.png":
        prompt = input ("référence: ")
        prompt = prompt + ".png"
        listeFichiers = []
        for (repertoire, sousRepertoires, fichiers) in walk("../"+search_directory):
            listeFichiers.extend(fichiers)
        #print(listeFichiers)
        if prompt in listeFichiers:
            print("found!")
            print(prompt)
            img = Image.open("../"+search_directory+"/"+prompt)
            img.show()
        else:
            print("not found!")
        
print("Goodbye young pilot!")