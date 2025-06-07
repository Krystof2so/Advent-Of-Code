# Jour 2 : Alarme du programme 1202

## Premier puzzle

Sur le chemin de l'[assistance gravitationnelle](https://fr.wikipedia.org/wiki/Assistance_gravitationnelle) autour de la Lune, l'ordinateur de bord émet un bip de colère à propos d'une « *alarme de programme 1202* ». A la radio, un Elfe est déjà en train d'expliquer comment gérer la situation : « *Ne vous inquiétez pas, c'est tout à fait normal*... » L'ordinateur de bord s'[enflamme](https://fr.wikipedia.org/wiki/Halt_and_Catch_Fire).

Vous informez les Elfes que la fumée magique de l'ordinateur semble s'être échappée. « *Cet ordinateur exécutait des programmes Intcode comme le programme d'assistance à la gravité sur lequel il travaillait ; il y a sûrement assez de pièces détachées là-haut pour construire un nouvel ordinateur Intcode !* »

Un programme Intcode est une liste d'[entiers](https://fr.wikipedia.org/wiki/Entier_relatif) séparés par des virgules (comme 1,0,0,3,99). Pour en exécuter un, commencez par regarder le premier entier (appelé position 0). Vous y trouverez un opcode - soit 1, 2 ou 99. L'opcode indique ce qu'il faut faire ; par exemple, 99 signifie que le programme est terminé et qu'il doit s'arrêter immédiatement. Si vous rencontrez un opcode inconnu, cela signifie que quelque chose n'a pas fonctionné.

L'opcode 1 additionne des nombres lus à partir de deux positions et stocke le résultat dans une troisième position. Les trois entiers qui suivent immédiatement l'opcode indiquent ces trois positions - les deux premiers indiquent les positions à partir desquelles vous devez lire les valeurs d'entrée, et le troisième indique la position à laquelle le résultat doit être stocké.

Par exemple, si votre ordinateur Intcode rencontre 1,10,20,30, il doit lire les valeurs aux positions 10 et 20, les additionner, puis remplacer la valeur à la position 30 par leur somme.

L'opcode 2 fonctionne exactement comme l'opcode 1, sauf qu'il multiplie les deux entrées au lieu de les additionner. Là encore, les trois entiers qui suivent l'opcode indiquent l'emplacement des entrées et des sorties, et non leurs valeurs.

Une fois le traitement d'un opcode terminé, passez au suivant en avançant de 4 positions.

Par exemple, supposons que vous ayez le programme suivant :
```txt
1,9,10,3,2,3,11,0,99,30,40,50
```

À titre d'illustration, voici le même programme divisé en plusieurs lignes :
```txt
1,9,10,3,
2,3,11,0,
99,
30,40,50
```

Les quatre premiers entiers, 1,9,10,3, se trouvent aux positions 0, 1, 2 et 3. Ensemble, ils représentent le premier opcode (1, addition), les positions des deux entrées (9 et 10) et la position de la sortie (3). Pour traiter cet opcode, vous devez d'abord obtenir les valeurs aux positions des entrées : la position 9 contient 30, et la position 10 contient 40. Additionnez ces nombres pour obtenir 70. Ensuite, stockez cette valeur à la position de sortie ; ici, la position de sortie (3) est à la position 3, donc elle s'écrase elle-même. Ensuite, le programme se présente comme suit :
```txt
1,9,10,70,
2,3,11,0,
99,
30,40,50
```

Avancez de 4 positions pour atteindre l'opcode suivant, 2. Cet opcode fonctionne comme le précédent, mais il multiplie au lieu d'additionner. Les entrées se trouvent aux positions 3 et 11 ; ces positions contiennent respectivement 70 et 50. En les multipliant, on obtient 3500, qui est stocké en position 0 :
```txt
3500,9,10,70,
2,3,11,0,
99,
30,40,50
```

En avançant de 4 positions supplémentaires, on arrive à l'opcode 99, ce qui arrête le programme.

Voici les états initiaux et finaux de quelques autres petits programmes :

   - 1,0,0,0,99 devient 2,0,0,0,99 (1 + 1 = 2).
   - 2,3,0,3,99 devient 2,3,0,6,99 (3 * 2 = 6).
   - 2,4,4,5,99,0 devient 2,4,4,5,99,9801 (99 * 99 = 9801).
   - 1,1,1,4,99,5,6,0,99 devient 30,1,1,4,2,5,6,0,99.

Une fois que vous avez un ordinateur en état de marche, la première étape consiste à rétablir le programme d'assistance gravitationnelle (votre entrée de puzzle) à l'état d'alarme du programme 1202 qu'il avait juste avant que le dernier ordinateur ne prenne feu. Pour ce faire, avant d'exécuter le programme, remplacez la position 1 par la valeur 12 et la position 2 par la valeur 2. Quelle valeur reste-t-il en position 0 après l'arrêt du programme ?

## Second puzzle

« *Bien, le nouvel ordinateur semble fonctionner correctement ! Gardez-le à proximité pendant cette mission - vous l'utiliserez probablement à nouveau. Les vrais ordinateurs Intcode supportent beaucoup plus de fonctionnalités que votre nouvel ordinateur, mais nous vous ferons savoir lesquelles au fur et à mesure que vous en aurez besoin*. "

« *Cependant, votre priorité actuelle devrait être de terminer votre assistance gravitationnelle autour de la Lune. Pour que cette mission soit couronnée de succès, nous devrions nous mettre d'accord sur une terminologie pour les pièces que vous avez déjà construites*. »

Les programmes Intcode sont présentés sous la forme d'une liste d'entiers ; ces valeurs sont utilisées comme état initial de la mémoire de l'ordinateur. Lorsque vous exécutez un programme Intcode, veillez à initialiser la mémoire aux valeurs du programme. Une position dans la mémoire est appelée adresse (par exemple, la première valeur dans la mémoire est à « l'adresse 0 »).

Les opcodes (comme 1, 2 ou 99) marquent le début d'une instruction. Les valeurs utilisées immédiatement après un opcode, le cas échéant, sont appelées les paramètres de l'instruction. Par exemple, dans l'instruction 1,2,3,4, 1 est l'opcode ; 2, 3 et 4 sont les paramètres. L'instruction 99 ne contient qu'un opcode et n'a pas de paramètres.

L'adresse de l'instruction en cours est appelée pointeur d'instruction ; elle commence à 0. À la fin d'une instruction, le pointeur d'instruction augmente du nombre de valeurs de l'instruction ; jusqu'à ce que vous ajoutiez d'autres instructions à l'ordinateur, ce nombre est toujours de 4 (1 opcode + 3 paramètres) pour les instructions d'addition et de multiplication. (L'instruction halt augmenterait le pointeur d'instruction de 1, mais elle arrête le programme à la place).

« La terminologie ayant été éliminée, nous sommes prêts à poursuivre. Pour compléter l'assistance gravitationnelle, vous devez déterminer quelle paire d'entrées produit la sortie 19690720. »

Les entrées doivent toujours être fournies au programme en remplaçant les valeurs aux adresses 1 et 2, comme auparavant. Dans ce programme, la valeur placée à l'adresse 1 est appelée le nom, et la valeur placée à l'adresse 2 est appelée le verbe. Chacune des deux valeurs d'entrée sera comprise entre 0 et 99 inclus.

Une fois que le programme s'est arrêté, sa sortie est disponible à l'adresse 0, comme auparavant. Chaque fois que vous essayez une paire d'entrées, assurez-vous d'abord de réinitialiser la mémoire de l'ordinateur aux valeurs du programme (votre entrée puzzle) - en d'autres termes, ne réutilisez pas la mémoire d'une tentative précédente.

Trouvez le nom et le verbe de l'entrée qui font que le programme produit la sortie 19690720. Quelle est la valeur de 100 * nom + verbe ? (Par exemple, si le nom = 12 et le verbe = 2, la réponse serait 1202).
