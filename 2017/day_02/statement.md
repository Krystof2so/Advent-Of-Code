# Jour 2 : Corruption du Checksum 

## Première partie

Alors que vous franchissez la porte, une forme humanoïde lumineuse crie dans votre direction. « *Vous êtes là ! Vous semblez être en état d'inactivité. Venez nous aider à réparer la corruption de cette feuille de calcul - si nous prenons une milliseconde de plus, nous devrons afficher un curseur en forme de sablier !* »

La feuille de calcul est constituée de lignes de nombres apparemment aléatoires. Pour s'assurer que le processus de récupération est sur la bonne voie, ils ont besoin que vous calculiez la somme de contrôle de la feuille de calcul. Pour chaque ligne, déterminez la différence entre la plus grande et la plus petite valeur ; la somme de contrôle est la somme de toutes ces différences.

Par exemple, si l'on considère la feuille de calcul suivante :
```txt
5 1 9 5
7 5 3
2 4 6 8
```

- La plus grande et la plus petite valeur de la première ligne sont 9 et 1, et leur différence est 8.
- La plus grande et la plus petite valeur de la deuxième ligne sont 7 et 3, et leur différence est de 4.
- La différence de la troisième ligne est de 6.

Dans cet exemple, la somme de contrôle de la feuille de calcul serait 8 + 4 + 6 = 18.

Quelle est la somme de contrôle de la feuille de calcul dans l'entrée de votre puzzle ?


## Seconde partie

« *Bon travail ; il semble que nous soyons sur la bonne voie après tout. Voici une étoile pour votre effort* ». Cependant, le programme semble un peu inquiet. Les programmes peuvent-ils être inquiets ?

« *D'après ce que nous voyons, il semble que tout ce que l'utilisateur voulait, c'était des informations sur les valeurs uniformément divisibles de la feuille de calcul. Malheureusement, aucun d'entre nous n'est équipé pour ce type de calcul - la plupart d'entre nous se spécialisent dans les opérations par bits.* »

Il semble que l'objectif soit de trouver les deux seuls nombres de chaque ligne dont l'un divise l'autre de manière égale - c'est-à-dire où le résultat de l'opération de division est un nombre entier. Ils aimeraient que vous trouviez ces nombres sur chaque ligne, que vous les divisiez et que vous additionniez le résultat de chaque ligne.

Par exemple, si l'on considère la feuille de calcul suivante :
```txt
5 9 2 8
9 4 7 3
3 8 6 5
```

- Dans la première ligne, les deux seuls nombres qui se divisent également sont 8 et 2 ; le résultat de cette division est 4.
-  Dans la deuxième ligne, les deux nombres sont 9 et 3 ; le résultat est 3.
-  Dans la troisième ligne, le résultat est 2.

Dans cet exemple, la somme des résultats est 4 + 3 + 2 = 9.

Quelle est la somme des résultats de chaque ligne dans votre puzzle ?

