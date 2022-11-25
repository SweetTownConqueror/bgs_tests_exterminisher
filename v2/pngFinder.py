from os import walk
from PIL import Image
import sys

print("Pass your destination folder as argument to search to specific folder (default: screenshots)")
print("q: quit")

search_directory = "./screenshots"
if len(sys.argv) == 2:
    search_directory = sys.argv[1]
    
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