# Mémoire en spirale 

## Première partie

Vous découvrez un nouveau type de mémoire expérimentale stockée sur une grille bidimensionnelle infinie.

Chaque case de la grille est attribuée selon un modèle en spirale, en commençant par un emplacement marqué 1, puis en comptant vers le haut tout en allant en spirale vers l'extérieur. Par exemple, les premières cases sont attribuées comme suit :

17 16 15 14 13
18 5 4 3 12
19 6 1 2 11
20 7 8 9 10
21 22 23---> ...

Bien que cette méthode soit très économe en espace (aucune case n'est sautée), les données demandées doivent être ramenées à la case 1 (l'emplacement du seul port d'accès pour ce système de mémoire) par des programmes qui ne peuvent se déplacer que vers le haut, le bas, la gauche ou la droite. Ils empruntent toujours le chemin le plus court : la distance de Manhattan entre l'emplacement des données et la case 1.

Par exemple, les données de la case 1 sont transportées à 0 pas de l'endroit où se trouvent les données :

    Les données de la case 1 sont transportées sur 0 pas, puisqu'elles se trouvent au port d'accès.
    Les données de la case 12 sont transportées sur 3 pas, par exemple : vers le bas, vers la gauche, vers la gauche.
    Les données de la case 23 ne sont transportées que sur 2 pas : vers le haut deux fois.
    Les données de la case 1024 doivent être transportées en 31 étapes.

Combien d'étapes sont nécessaires pour transporter les données de la case identifiée dans votre puzzle jusqu'au port d'accès ?

L'entrée de votre puzzle est 361527.

## Seconde partie

Pour tester le système, les programmes effacent la grille et stockent la valeur 1 dans la case 1. Ensuite, dans le même ordre d'allocation que celui indiqué ci-dessus, ils stockent la somme des valeurs dans toutes les cases adjacentes, y compris les diagonales.

Les valeurs des premières cases sont donc choisies comme suit :

    La case 1 commence avec la valeur 1.
    La case 2 n'a qu'une seule case adjacente remplie (avec la valeur 1), elle stocke donc également 1.
    La case 3 a pour voisines les deux cases ci-dessus et enregistre la somme de leurs valeurs, soit 2.
    La case 4 a pour voisines les trois cases susmentionnées et enregistre la somme de leurs valeurs, 4.
    La case 5 n'a pour voisins que la première et la quatrième case, et reçoit donc la valeur 5.

Une fois qu'une case est écrite, sa valeur ne change pas. Par conséquent, les premières cases recevront les valeurs suivantes :

147 142 133 122 59
304 5 4 2 57
330 10 1 1 54
351 11 23 25 26
362 747 806---> ...

Quelle est la première valeur écrite qui est plus grande que l'entrée de votre puzzle ?

