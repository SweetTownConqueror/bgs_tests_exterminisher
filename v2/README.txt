Recap commandes:
aller dans le dossier python et exécuter dans le cmd:
python ../pngFinder.py screenshots/
python ../main.py -parse nombre_de_questions
python ../main.py -screen nombre_de_questions

Ce script python 3.11.0 a été testé sous windows 10 avec l'application BGS en plein écran, version à l'ordre du jour ce 23/11/2022 avec
un écran de résolution 1920x1080

Est la V2 de cet outil.

Il permet toujours de valider un test:

python ../main.py -parse nombre_de_questions

Lorsque l'on arrive sur la correction d'un test, on peut récupérer les screenshots de la correction:

python ../main.py -screen nombre_de_questions

Le script va alors parcourir une à une les questions corrigée, en faire un screenshot, et le sauvegarder dans le dossier screenshot...
Avec pour titre la référence de la question!!!

C'est ce qui fait la merveille technologique de cet outil.
Le script va en background faire une capture de la zone où il y a la référence, extraire de cette capture la référence sous forme de texte
grâce à la librairie tesseract (permet d'extraire du texte d'une image), et nommer le screenshot du numéro de référene ainsi récupérée.


Une fois que vous tombé en test sur une question que vous ne connaissez pas, vous n'avez plus qu'à rechercher le screenshot portant la
référence de la question. Un prochain outil est à venir pour faciliter ce travail de recherche et ne plus perdre de temps à chercher les questions
via l'explorateur de windows par défault.


TODO:

-Mettre un argument pour définir le pas qui est d'environ 66 par défaut mais qui peut varier légèrement selon les tests afin que pour les longues séries
Le script clique le plus au milieu possible du bouton de la question
-quand il y a plus de 26 questions il faut refaire un pas décalé un peu plus important
-on pourrait mettre en place un script déclenché par un raccourci ou par commande qui determine la referrence de la question en cours,
fait appel au script pour chercher la question et ouvre directement la reponse: on a ainsi plus qu'à cliquer sans devoir chercher manuellement
chaque reponse


Update: 
le programme permettant de faciliter la recherche d'un fihier png est maintenant prêt.
Pour le lancer: 
python ../pngFinder.py screenshots/
Vous pouvez passer en argument le chemin vers le dossier sur lequel vous voulez effectuer la recherche de votre question.
Vous ne devez qu'entrer la référence de la question, le programme se charge de la chercher parmi les noms des captures crées automatiquement 
précédement.