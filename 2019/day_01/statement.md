# Jour 1 : La tyrannie de l'équation de la fusée

## Première partie

Le Père Noël s'est retrouvé bloqué aux confins du système solaire alors qu'il livrait des cadeaux à d'autres planètes ! Pour calculer avec précision sa position dans l'espace, aligner en toute sécurité son moteur à distorsion et revenir sur Terre à temps pour sauver Noël, il a besoin que vous lui apportiez des mesures provenant de cinquante étoiles.

Collectez des étoiles en résolvant des énigmes. Deux énigmes seront disponibles chaque jour du calendrier de l'Avent ; la deuxième énigme sera débloquée lorsque vous aurez terminé la première. Chaque puzzle donne droit à une étoile. Bonne chance !

Les Elfes vous chargent rapidement dans un vaisseau spatial et se préparent à le lancer.

Au premier sondage Go / No Go, tous les Elfes sont Go jusqu'au compteur de carburant. Ils n'ont pas encore déterminé la quantité de carburant nécessaire.

Le carburant nécessaire au lancement d'un module donné est fonction de sa masse. Plus précisément, pour déterminer le carburant nécessaire pour un module, il faut prendre sa masse, la diviser par trois, arrondir à l'unité inférieure et soustraire 2.

Par exemple, pour une masse de 12, il faut diviser par 3 et arrondir à 4 :

    Pour une masse de 12, on divise par 3 et on arrondit à l'unité inférieure pour obtenir 4, puis on soustrait 2 pour obtenir 2.
    Pour une masse de 14, en divisant par 3 et en arrondissant à l'unité inférieure, on obtient toujours 4, donc le carburant nécessaire est également de 2.
    Pour une masse de 1969, le carburant nécessaire est de 654.
    Pour une masse de 100756, le carburant nécessaire est 33583.

Le compteur de carburant doit connaître le besoin total en carburant. Pour ce faire, calculez individuellement le carburant nécessaire pour la masse de chaque module (votre entrée de puzzle), puis additionnez toutes les valeurs de carburant.

Quelle est la somme des besoins en carburant de tous les modules de votre vaisseau spatial ?

## Seconde partie

Au cours du deuxième sondage Go / No Go, l'elfe chargé de la double vérification de l'équation de la fusée interrompt la séquence de lancement. Apparemment, vous avez oublié d'inclure du carburant supplémentaire pour le carburant que vous venez d'ajouter.

Le carburant lui-même nécessite du carburant, tout comme un module - prenez sa masse, divisez-la par trois, arrondissez-la à l'unité inférieure et soustrayez 2. Cependant, ce carburant nécessite également du carburant, et ce carburant nécessite du carburant, et ainsi de suite. Toute masse qui nécessiterait un carburant négatif doit être traitée comme si elle nécessitait zéro carburant ; la masse restante, s'il y en a une, est traitée en souhaitant très fort qu'elle ait si peu de masse pour ne pas entrer dans le cadre de ce calcul.

Ainsi, pour chaque masse de module, calculez son carburant et ajoutez-le au total. Ensuite, considérez la quantité de carburant que vous venez de calculer comme la masse d'entrée et répétez le processus, jusqu'à ce que le besoin en carburant soit nul ou négatif. Par exemple :

- Un module de masse 14 nécessite 2 combustibles. Ce carburant ne nécessite aucun autre carburant (2 divisé par 3 et arrondi à l'inférieur donne 0, ce qui nécessiterait un carburant négatif), de sorte que le carburant total nécessaire n'est toujours que de 2.
- Dans un premier temps, un module de masse 1969 nécessite 654 combustibles. Ensuite, ce combustible nécessite 216 combustibles supplémentaires (654 / 3 - 2). 216 nécessite ensuite 70 combustibles supplémentaires, qui nécessitent 21 combustibles, qui nécessitent 5 combustibles, qui ne nécessitent aucun combustible supplémentaire. Ainsi, le carburant total requis pour un module de masse 1969 est de 654 + 216 + 70 + 21 + 5 = 966.
- Le carburant requis par un module de masse 100756 et son carburant est : 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

Quelle est la somme des besoins en carburant de tous les modules de votre vaisseau spatial en tenant compte de la masse du carburant ajouté ? (Calculez les besoins en carburant de chaque module séparément, puis additionnez-les à la fin).

