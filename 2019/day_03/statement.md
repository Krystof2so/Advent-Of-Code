# Crossed Wires 

## Première partie

L'assistance gravitationnelle a réussi et vous êtes en bonne voie pour atteindre la station de ravitaillement de Vénus. Dans la précipitation du retour sur Terre, le système de gestion du carburant n'a pas été complètement installé, c'est donc la prochaine étape sur la liste des priorités.

En ouvrant le panneau avant, on découvre un enchevêtrement de fils. Plus précisément, deux fils sont connectés à un port central et s'étendent vers l'extérieur sur une grille. Vous tracez le chemin que prend chaque fil lorsqu'il quitte le port central, un fil par ligne de texte (votre entrée dans le puzzle).

Les fils se tordent et tournent, mais les deux fils se croisent de temps en temps. Pour réparer le circuit, vous devez trouver le point d'intersection le plus proche du port central. Les fils étant disposés sur une grille, utilisez la distance de Manhattan pour cette mesure. Bien que les fils se croisent techniquement au niveau du port central où ils commencent tous les deux, ce point ne compte pas, et un fil ne compte pas non plus comme se croisant avec lui-même.

Par exemple, si le chemin du premier fil est R8,U5,L5,D3, alors en partant du port central (o), il va à droite 8, en haut 5, à gauche 5, et enfin en bas 3 :

```txt
...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
```

Ensuite, si le chemin du deuxième fil est U7,R6,D4,L4, il va vers le haut 7, vers la droite 6, vers le bas 4 et vers la gauche 4 :

```txt
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

Ces fils se croisent à deux endroits (marqués X), mais celui en bas à gauche est plus proche du port central : sa distance est de 3 + 3 = 6.

Voici quelques autres exemples :

    R75,D30,R83,U83,L12,D49,R71,U7,L72
 U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
 R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
 U98, R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

Quelle est la distance de Manhattan entre le port central et l'intersection la plus proche ?

## Seconde partie

Il s'avère que ce circuit est très sensible au temps ; vous devez en fait minimiser le retard du signal.

Pour ce faire, calculez le nombre de pas que chaque fil met pour atteindre chaque intersection ; choisissez l'intersection où la somme des pas des deux fils est la plus faible. Si un fil visite plusieurs fois une position sur la grille, utilisez la valeur des pas de la première fois qu'il visite cette position pour calculer la valeur totale d'une intersection spécifique.

```txt
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

Dans l'exemple ci-dessus, l'intersection la plus proche du port central est atteinte après 8+5+5+2 = 20 pas par le premier fil et 7+6+4+3 = 20 pas par le deuxième fil, soit un total de 20+20 = 40 pas.

Cependant, l'intersection en haut à droite est meilleure : le premier fil ne prend que 8+5+2 = 15 et le second fil ne prend que 7+6+2 = 15, soit un total de 15+15 = 30 pas.

Voici les meilleures étapes pour les exemples supplémentaires ci-dessus :

    R75,D30,R83,U83,L12,D49,R71,U7,L72
 U62,R66,U55,R34,D71,R55,D58,R83 = 610 étapes
 R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
 U98, R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 pas

Quel est le plus petit nombre de pas combinés que les fils doivent faire pour atteindre une intersection ?


