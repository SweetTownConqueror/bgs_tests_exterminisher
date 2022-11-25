RECAP commandes:
aller dans le dossier python et exécuter dans le cmd:
python ../main.py --xoffset 0 --yoffset 0 --questions 5
à lancienn cousin:
python ../pngFinder.py screenshots/
comme un boss bogoss:
python ../fillTest.py --dir perfo



Ce script python 3.11.0 a été testé sous windows 10 avec l'application BGS en plein écran, version à l'ordre du jour ce 23/11/2022 avec
un écran de résolution 1920x1080

Description:
Ceci est la version 3.1 version bien plus simplifiée et efficace de la 3.0
Comme les autres versions elle est ultra portative et peut s'executer depuis une clé usb.
Pour exécuter les commandes fournies bien veiller à etre dans le dossier python.
Plus besoin, de s'embeter à parcourir 2 3 4 voir plus de tests à corriger pour obtenir toutes les questions corrigée,
car j'ai découvert une astuce: 
On peut se rendre sur le site de BGS et voir toutes les questions corrigée de la banque BGS, cependant vu qu'il y en a beaucoup trop
il est difficile de sélectionner seules celles qui nous intéresse pour remplir un test que l'on souhaite passer.
C'est là que mon programme intervient.

Il est simplifié car désormais: 
-Pour passer d'une question à une autre il n'y a plus d'histoire de pitch, mais la souris clique simplement
sur le bouton suivant à droite de l'écran. Il n'y a donc plus de paramètre --pitch à passer au script
C'était tout simple mais il fallait y penser!
-Le script ne prend plus de paramètre --action car il n'y a maintenant plus besoin de parcourir un test pour récupérer la correction
car on peut directement avoir accès à toutes les questions corrigées de la base de BGS. Le script ne fera donc plus que des captures des
questions corrigées.

Pour lancer le script, la commande est alors:

python ../main.py --xoffset 0 --yoffset 0 --questions 10

--------------------------------------------------------------------------------------------------------------------------------------------
MODE D'EMPLOI
--------------------------------------------------------------------------------------------------------------------------------------------

I Récupérer la correction de toutes les question d'un sujet

1)Allez sur : https://qbank.bgsonline.eu/dashboard, cliquez en bas sur exams, choisissez votre sujet, cliquez sur show answers "before choice"
Puis start test
3)Mettez votre navigateur en plein écran et dans le dossier python lancez la commande suivante:
python ../main.py --xoffset 0 --yoffset 0 --questions 5
4)Si le script ne passe pas à la question suivante jouer sur les parametres --xoffset et --yoffset pour le faire cliquer sur le bouton
question suivante
5)Si les captures ne se font pas aller à la section PROBLEMES en bas de cette page:
	->1)Trop de mes titres de captures ne sont pas nommées correctement ou mes captures ne se font pas
6)Le programme va maintenant parcourir toutes les questions corrigées de la matière sélectionnée et en faire une capture et 
l'enregistrer dans screenshots.
8)Maintenant que vous avez toutes les questions de la base de donnée pour une matière, vous pourrez remplir tous les tests de cette matière
grâce aux méthodes inchangées:
A L'ANCIENN COUSIN
ou bien 
COMME UN BOSS BOGOSS

		-----------------------------------------------------------------------------------------------------------
II Remplir avec succès un test
II A l'ANCIENN COUSIN

1) Allez sur votre test BGS
2) Lancez le script suivant: python ../pngFinder.py --dir cheminvers/votredossiercontenantvoscapturesdeletapeII , ex:
python ../pngFinder.py --dir screenshots/fpl
3)Regardez la référence de la question
4) Entrez la référence dans le programme. S'il trouve la question il ouvre directement la capture de la correction associée 
et s'il ne la trouve pas il vous prévient: not found!
5) Faites de même pour toutes les questions du test

NOTE:
Pour les tests qui ont beaucoup de questions, c'est redondant de devoir taper 100 fois la référence à chaque fois,
Voici pourquoi j'ai développé la méthode COMME UN BOSS BOGOSS

II COMME UN BOSS BOGOSS

1) Allez sur votre test BGS (en plein écran bien sur!)
2) Lancez le script suivant: python ../fillTest.py --dir cheminvers/votredossiercontenantvoscapturesdeletapeII , ex:
python ../fillTest.py --dir flightplanning
3) Si le script trouve la question il l'ouvre automatiquement sinon il affiche not found
4) Remplissez ainsi toutes les questions du test et obtenez un super score!
5) Good luck young pilot;)

NOTE: 
Il faut que le dossier qui contient les capture soit dans le dossiers screenshot!
Attention à ce que le chemin spécifié soit correct sinon il ne vous trouvera pas la capture que vous cherchez!
Si le programme ne trouve pas la question, rendez vous en bas section PROBLEMES:
	->1)Trop de mes titres de captures ne sont pas nommées correctement, mes captures ne se font pas ou mes questions 
de test ne sont pas trouvées
Astuce:
Vous pouvez:
-Créer un fichier .bat dans le dossier python, avec dedans quelque chose comme:
python ../fillTest.py --dir gnav
-Créer un raccourci de ce .bat et mettre le racourci sur le bureau en bas de l'écran
-Votre BGS en plein écran, relever juste le bas de l'appli pour voir le raccourci sur le bureau
-Vous pouvez maintenant d'un seul clic lancer le programme qui va détecter la question de votre test et ouvrir la capture correspondante
avec la correction

--------------------------------------------------------------------------------------------------------------------------------------------
PROBLEMES
--------------------------------------------------------------------------------------------------------------------------------------------
1)Trop de mes titres de captures ne sont pas nommées correctement ou mes captures ne se font pas
	a)Vérifiez que vous êtes bien avec BGS en plein écran lorsque vous effectuez ce script, sinon
	b)Regardez dans le dossier tmp la capture correspondant à la zone contenant la référence de la question.
Ci cette dernière est coupée où que vous voyez une autre partie de l'écran dessus, ouvrez le fichier main.py avec un éditeur de texte
tel que sublime text ou notepad ++, rendez vous à la ligne contenant: im=ImageGrab.grab(bbox=(1600,350,1752,420))
et 		b1) jouez sur ces 4 chiffre
		b2)Relancez le script
		b3)Recommenez b1 et b2 jusqu'à ce que la capture soit centrée sur la partie de l'écran contenant  
"Ref: numeroquestion
Score: scorequestion"
		b4)Il faut que le dernier chiffre de la référence de la question effleure le bord droit de la capture, c'est très important
à 1 ou 2 pixel près l'extraction de la référence de la question sera incorrecte. Pour celà jouer sur ce paramètre:
im=ImageGrab.grab(bbox=(1600,350,XXXX,420))



