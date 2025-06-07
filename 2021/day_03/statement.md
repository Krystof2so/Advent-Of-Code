# Jour 3 : Diagnostic binaire

## Première partie

Votre sous-marin a été conçu de manière à pouvoir fonctionner de manière sûre à des profondeurs considérables sous la surface de l'océan. Il est équipé d'un système de diagnostic qui utilise des codes de diagnostic binaires pour vérifier que tout fonctionne correctement.

Vous avez téléchargé un rapport de diagnostic (votre entrée de puzzle) depuis le sous-marin pour essayer de déterminer la cause du problème. Le rapport de diagnostic est une liste de nombres binaires qui, selon le fabricant du sous-marin, peuvent être utilisés pour diagnostiquer de nombreuses conditions courantes.

La première étape pour vérifier que le système de diagnostic fonctionne correctement est de vérifier le taux d'erreur binaire (binary diagnostic rate). Pour ce faire, vous devez calculer le taux gamma et le taux epsilon à partir du rapport de diagnostic.

Le taux gamma peut être déterminé en trouvant le bit le plus courant (0 ou 1) dans la position correspondante pour tous les nombres du rapport de diagnostic. Par exemple, étant donné le rapport de diagnostic suivant :
```txt
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

En considérant uniquement le premier bit de chaque nombre, il y a cinq 0 et sept 1. Puisque le bit le plus courant est 1, le premier bit du taux gamma est 1.

Le bit le plus courant pour la deuxième position est 0, et ainsi de suite. Donc, le taux gamma pour le rapport de diagnostic ci-dessus est 10110, soit 22 en décimal.

Le taux epsilon est calculé de manière similaire ; plutôt que d'utiliser le bit le plus courant, il utilise le bit le moins courant pour chaque position. Donc, le taux epsilon est 01001, soit 9 en décimal.

En multipliant le taux gamma (22) par le taux epsilon (9), on obtient le taux d'erreur binaire, qui dans cet exemple est 198.

En utilisant le rapport de diagnostic de votre puzzle, calculez le taux gamma et le taux epsilon, puis multipliez-les ensemble. Quel est le taux d'erreur binaire de votre sous-marin ? (Assurez-vous de représenter votre réponse en décimal, pas en binaire.)


## seconde partie

Ensuite, vous devez vérifier le système de support vie, qui génère des nombres binaires pour spécifier quels bits doivent être vérifiés. Cependant, au lieu de calculer le taux gamma et le taux epsilon, vous devez déterminer le taux d'oxygène et le taux de CO2.

Le taux d'oxygène est déterminé en trouvant le nombre binaire le plus courant dans le rapport de diagnostic, en utilisant un processus similaire à celui utilisé pour trouver le taux gamma. Cependant, plutôt que de considérer tous les bits en même temps, vous devez considérer un bit à la fois, en commençant par le bit le plus significatif. Pour chaque bit considéré, vous filtrez la liste de nombres pour ne garder que ceux qui ont le bit le plus courant dans cette position. Si 0 et 1 sont également courants, gardez les nombres qui ont un 1 dans cette position. Répétez ce processus jusqu'à ce qu'il ne reste qu'un seul nombre, qui sera le taux d'oxygène.

Le taux de CO2 est déterminé de manière similaire, mais en gardant les nombres qui ont le bit le moins courant dans chaque position. Si 0 et 1 sont également courants, gardez les nombres qui ont un 0 dans cette position.

Enfin, multipliez le taux d'oxygène par le taux de CO2 pour obtenir le taux de support vie du sous-marin. Quel est le taux de support vie de votre sous-marin ? (Assurez-vous de représenter votre réponse en décimal, pas en binaire.)

Pour résoudre ce problème, vous devez lire et analyser les nombres binaires du rapport de diagnostic, calculer les taux gamma et epsilon pour la première partie, et les taux d'oxygène et de CO2 pour la seconde partie. Ensuite, vous devez multiplier les taux obtenus pour obtenir les résultats finaux.
