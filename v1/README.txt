Ce script python 3.11.0

Permet de valider un test de BGS en cliquant sur un question, cliquant une réponse puis cliquant la question suivante, etc...

Pour ce faire: python ../main.py -parse nombre_de_questions

Une fois le résultat obtenu, il permet de parcourir chaque question de la correction pour avoir la réponse pour chacune de ces questions

Pour ce faire: python ../main.py -screen nombre_de_questions


Nb:
La fonction parse ne semble peut être pas judicieuse car après tout on pourrait simplement valider le test vide pour avoir
la correction et passer directement au 2 eme script pour récupérer les bonnes réponse de toutes les questions,
mais je pense qu'il y a des chances que celà paraisse suspects aux modérateurs et instructeurs qui regarderont les résultats.

TODO:
Un fonction qui va chercher la référence de la question dans l'image pour pouvoir directement nommer correctement le screenshot
du numéro de la question

Une fois que chaque screenshot sera sauvegardé avec un numéro adéquat il faudra un script qui attendra en permanence qu'on lui entre
une reference de question.
Si la reference est dans un des noms de screenshot on laffiche sinon: not found! et on attend une autre référence