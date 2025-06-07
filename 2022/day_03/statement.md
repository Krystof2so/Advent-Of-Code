# Réarrangement du Sac à Dos

## Première partie

Vous êtes en train de préparer vos affaires pour une expédition dans la jungle. Chaque groupe de trois Elfes doit avoir un badge distinct pour des raisons de sécurité. Cependant, les Elfes ont du mal à se mettre d'accord sur l'attribution des objets dans leurs sacs à dos.

Chaque Elfe a une liste d'objets dans son sac à dos, mais ils ne sont pas bien organisés. Chaque ligne de votre liste d'objets représente le contenu d'un sac à dos. Par exemple, voici une liste d'objets pour six Elfes :
```txt
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

Pour faciliter la recherche des objets en double, chaque Elfe a divisé son sac à dos en deux compartiments. La première moitié des caractères représente le premier compartiment, et la seconde moitié représente le second compartiment.

Par exemple, le premier sac à dos contient les objets suivants :
```txt
vJrwpWtwJgWrhcsFMMfFFhFp
```

Ici, le premier compartiment contient `vJrwpWtwJgWr`, et le second compartiment contient `hcsFMMfFFhFp`. L'objet en double dans ce sac à dos est `p`.

Voici les objets en double pour les autres sacs à dos :
```txt
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL : L
PmmdzqPrVvPwwTWBwg : P
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn : v
ttgJtRGJQctTZtZT : t
CrZsJsPPZsGzwwsLwLmpwMDw : s
```

Les priorités des objets sont déterminées par leur position dans l'alphabet, où `a` a une priorité de 1, `b` a une priorité de 2, et ainsi de suite jusqu'à `z` qui a une priorité de 26. Les lettres majuscules ont des priorités de 27 à 52, où `A` a une priorité de 27, `B` a une priorité de 28, et ainsi de suite jusqu'à `Z` qui a une priorité de 52.

La somme des priorités des objets en double pour ces sacs à dos est 157 (16 pour `p`, 38 pour `L`, 42 pour `P`, 22 pour `v`, 20 pour `t`, et 19 pour `s`).

Trouvez l'objet qui apparaît dans les deux compartiments de chaque sac à dos. Quel est la somme des priorités de ces objets ?

## Seconde partie 

En continuant à préparer vos affaires, vous réalisez que chaque groupe de trois Elfes doit avoir un badge distinct pour des raisons de sécurité. Cependant, les Elfes ont du mal à se mettre d'accord sur l'attribution des badges.

Chaque groupe de trois lignes dans votre liste représente un groupe distinct d'Elfes. Par exemple, voici un groupe de trois Elfes :
```txt
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
```

Le badge pour ce groupe est l'objet qui apparaît dans les sacs à dos des trois Elfes. Dans l'exemple ci-dessus, le seul objet qui apparaît dans les trois sacs à dos est `r`, donc `r` est le badge de ce groupe.

Voici les badges pour les autres groupes de trois Elfes :
```txt
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn, ttgJtRGJQctTZtZT, CrZsJsPPZsGzwwsLwLmpwMDw : Z
vJrwpWtwJgWrhcsFMMfFFhFp, jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL, PmmdzqPrVvPwwTWBwg : r (déjà traité)
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn, ttgJtRGJQctTZtZT, CrZsJsPPZsGzwwsLwLmpwMDw : Z (déjà traité)
```
La somme des priorités des badges pour ces groupes est 70 (18 pour `r`, 52 pour `Z`, et encore 52 pour `Z`).

Trouvez l'objet qui apparaît dans les sacs à dos des trois Elfes de chaque groupe. Quel est la somme des priorités de ces badges ?
