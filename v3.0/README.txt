RECAP commandes:
aller dans le dossier python et exécuter dans le cmd:
python ../main.py --action parse --pitch 61 --xoffset 0 --questions 5
python ../main.py --action screen --pitch 61 --xoffset 0 --questions 5
à lancienn cousin:
python ../pngFinder.py screenshots/
comme un boss bogoss:
python ../fillTest.py --dir perfo






Ce script python 3.11.0 a été testé sous windows 10 avec l'application BGS en plein écran, version à l'ordre du jour ce 23/11/2022 avec
un écran de résolution 1920x1080

Ceci mesdames et messieurs est la V3 de cet outil pour torcher les tests BGS.

Les scripts précédents on été modifié et l'appel se fait de façon maintenant différente.

Il y a également un nouveau script.

Voici le détail de chacun de ces scripts et le mode d'utilisation.



--------------------------------------------------------------------------------------------------------------------------------------------
MODE D'EMPLOI
--------------------------------------------------------------------------------------------------------------------------------------------

I Remplir un test BGS avec des valeurs aléatoires

1)Rendez vous sur un test BGS que vous devez valider et mettez le en plein écran
2)allez dans le dossier "python"
3)Ouvrez un cmd dans ce dossier et Lancez le script main.py avec la commande suivante: 
python ../main.py --action parse --pitch 61 --xoffset 0 --questions 5
4)Regardez si le pitch est correct sur les 5 premières questions, modifier ce paramètre en fonction. Par défaut le pitch est 61 
5)Lancez la commande suivante:
python ../main.py --action parse --pitch 61 --xoffset 0 --questions nombre_de_question

NOTE: 
S'il y a plus de 26 questions le test BGS devrait s'afficher en 2 pages.
Il faut alors executer la commande : 
python ../main.py --action parse --pitch 61 --xoffset 0 --questions 26
Sur la première page, puis se rendre sur la 2 eme page et relancer le script avec un offset de 50 avec la commande:
python ../main.py --action parse --pitch 61 --xoffset 50 --questions nombre_de_question_restantes

6) Votre test est maintenant rempli, s'il y a quelques questions qui n'ont pas été cochées, revenez dessus et cochez au hasard
7)Validez le test admirez votre score pourri et cliquer sur refaire le test
8)Vous pouvez maintenant passez à l'étape suivante pour récupérer des captures de la correction du test

		-----------------------------------------------------------------------------------------------------------
II Récupérer des captures de la correction du test

1)Rendez vous sur votre test BGS corrigé
2)Lancez la commande suivante:
python ../main.py --action screen --pitch 61 --xoffset 0 --questions 5
3)Regardez si le pitch est correct sur les 5 premières questions, modifier ce paramètre en fonction. Par défaut le pitch est 61
4)Lancez la commande suivante:
python ../main.py --action screen --pitch 61 --xoffset 0 --questions nombre_de_questions

NOTE:
S'il y a plus de 26 questions le test BGS devrait s'afficher en 2 pages.
Il faut alors executer la commande : 
python ../main.py --action screen --pitch 61 --xoffset 0 --questions 26
Sur la première page, puis se rendre sur la 2 eme page et relancer le script avec un offset de 50 avec la commande:
python ../main.py --action parse --pitch 61 --xoffset 50 --questions nombre_de_question_restantes

Vous devez maintenant avoir toutes vos questions capturées dans le dossier screenshot avec pour nom de capture la référence de la question.
En général les références font 6 chiffres. Vérifiez que vous avez bien 6 chiffres sur vos noms de captures.
Si ce n'est pas le cas ouvrez la capture regardez le numéro de la question et renommez votre capture.
S'il y a trop de captures avec un titre incorrect, rendez vous dans la section PROBLEMES -> 1)un peu plus bas

Vous pouvez maintenant mettre vos captures dans un dossier adéquat comme flightPlanning, MassAndBalance, ...
Mais faites attention, ce dossier DOIT être dans le dossier "screenshots"
Maintenant que vous avez la correction du test vous pouvez recommencer ce test et passer à l'étape suivante: 
A L'ANCIENN COUSIN
ou bien 
COMME UN BOSS BOGOSS

		-----------------------------------------------------------------------------------------------------------
III Recommencez le test
III A l'ANCIENN COUSIN

1) Allez sur votre test BGS où vous avez eût un score de minable aux étapes précédentes
2) Lancez le script suivant: python ../pngFinder.py --dir cheminvers/votredossiercontenantvoscapturesdeletapeII , ex:
python ../pngFinder.py --dir screenshots/fpl
3)Regardez la référence de la question
4) Entrez la référence dans le programme. S'il trouve la question il ouvre directement la capture de la correction associée 
et s'il ne la trouve pas il vous prévient: not found!
5) Faites de même pour toutes les questions du test

NOTE:
Attention à ce que le chemin spécifié soit correct sinon il ne vous trouvera pas la capture que vous cherchez!
Ne rentrez que la référence de la question que vous cherchez (nombre à 6 chiffres en général)
En général pour valider un progress test il faut 1 étape I, refaire l'étape II 2 fois et faire l'étape III une fois

Pour les tests qui ont beaucoup de questions, c'est redondant de devoir taper 100 fois la référence à chaque fois,
Voici pourquoi j'ai développé la méthode COMME UN BOSS BOGOSS

III COMME UN BOSS BOGOSS

1) Allez sur votre test BGS où vous avez eût un score de minable aux étapes précédentes (en plein écran bien sur!)
2) Lancez le script suivant: python ../pngFinder.py --dir cheminvers/votredossiercontenantvoscapturesdeletapeII , ex:
python ../fillTest.py --dir flightplanning
3) Si le script trouve la question il l'ouvre automatiquement sinon il affiche not found
4) Remplissez ainsi toutes les questions du test et obtenez un super score!
5) Good luck young pilot;)

NOTE: 
Il faut que le dossier qui contient les capture soit dans le dossiers screenshot!
Attention à ce que le chemin spécifié soit correct sinon il ne vous trouvera pas la capture que vous cherchez!
En général pour valider un progress test il faut 1 étape I, et refaire l'étape II et III 2 fois
















--------------------------------------------------------------------------------------------------------------------------------------------
PROBLEMES
--------------------------------------------------------------------------------------------------------------------------------------------
1)Trop de mes titres de captures ne sont pas nommées correctement
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



