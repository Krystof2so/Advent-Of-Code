# Trajectoire de la luge 

## Première partie

Une fois les problèmes de connexion résolus, vous vous mettez en route vers l'aéroport. Si voyager en luge est facile, ce n'est certainement pas sans danger : la maniabilité est très réduite et la zone est couverte d'arbres. Vous devrez déterminer les angles qui vous permettront de passer près du moins d'arbres possible.

En raison de la géologie locale, les arbres de cette zone ne poussent qu'à des coordonnées entières exactes dans une grille. Vous créez une carte (votre entrée de puzzle) des cases ouvertes (**.**) et des arbres (**#**) que vous pouvez voir. Par exemple :

```txt
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

Mais ce ne sont pas les seuls arbres ; en raison d'un article que vous avez lu un jour sur la génétique arboricole et la stabilité des biomes, le même schéma se répète plusieurs fois vers la droite :

```txt
..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

Vous commencez sur la case ouverte (**.**) dans le coin supérieur gauche et devez atteindre le bas (sous la ligne la plus basse de votre carte).

La luge ne peut suivre que quelques pentes spécifiques (vous avez opté pour un modèle moins cher qui préfère les nombres rationnels) ; commencez par compter tous les arbres que vous rencontreriez pour la pente droite 3, descente 1 :

À partir de votre position de départ en haut à gauche, vérifiez la position qui se trouve à droite 3 et en bas 1. Ensuite, vérifiez la position qui se trouve à droite 3 et en bas 1 à partir de là, et ainsi de suite jusqu'à ce que vous dépassiez le bas de la carte.

Les emplacements que vous vérifieriez dans l'exemple ci-dessus sont marqués ici par un O lorsqu'il y avait une case libre et par un X lorsqu'il y avait un arbre :

```txt
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

En partant du coin supérieur gauche de votre carte et en suivant une pente de 3 vers la droite et de 1 vers le bas, combien d'arbres rencontrerez-vous ?

## Seconde partie

Il est temps de vérifier le reste des pentes - après tout, vous devez minimiser la probabilité d'un arrêt soudain contre un arbre.

Déterminez le nombre d'arbres que vous rencontreriez si, pour chacune des pentes suivantes, vous partiez du coin supérieur gauche et traversiez la carte jusqu'en bas :

- À droite 1, en bas 1.
- À droite 3, en bas 1. (C'est la pente que vous avez déjà vérifiée.)
- 5 à droite, 1 vers le bas.
- 7 à droite, 1 vers le bas.
- 1 à droite, 2 vers le bas.

Dans l'exemple ci-dessus, ces pentes rencontreraient respectivement 2, 7, 3, 4 et 2 arbres ; multipliés ensemble, cela donne la réponse 336.

Que obtenez-vous si vous multipliez ensemble le nombre d'arbres rencontrés sur chacune des pentes répertoriées ?
