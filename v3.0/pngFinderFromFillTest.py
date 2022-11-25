from os import walk
from PIL import Image
import sys


def find_ref(ref, directory):
    search_directory = "../screenshots/"
    if directory != "":
        search_directory = "../screenshots/"+directory+"/"
        
    reference = ref + ".png"
    listeFichiers = []
    for (repertoire, sousRepertoires, fichiers) in walk(search_directory):
        listeFichiers.extend(fichiers)
        break;
    #print(listeFichiers)
    if reference in listeFichiers:
        print("found!")
        print(ref)
        img = Image.open(search_directory+reference)
        img.show()
    else:
        print(search_directory+reference)
        print("not found!")