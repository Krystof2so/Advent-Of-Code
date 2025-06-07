# Pierre Papier Ciseaux

## Première partie

Les elfes commencent à installer leur campement sur la plage. Pour décider quelle tente sera la plus proche de la réserve de snacks, un tournoi géant de pierre-papier-ciseaux est déjà en cours.

La pierre-papier-ciseaux est un jeu qui se joue à deux. Chaque partie comporte plusieurs tours ; à chaque tour, les joueurs choisissent simultanément l'une des trois options suivantes : Pierre, Papier ou Ciseaux, à l'aide d'une forme de main. Ensuite, un gagnant est désigné pour ce tour : Pierre bat Ciseaux, Ciseaux bat Papier et Papier bat Pierre. Si les deux joueurs choisissent la même forme, la manche se termine par un match nul.

Reconnaissant de l'aide que vous lui avez apportée hier, un Elfe vous donne un guide de stratégie crypté (votre entrée d'énigme) qui, selon lui, vous aidera à gagner. «*La première colonne indique ce que votre adversaire va jouer : A pour Pierre, B pour Papier et C pour Ciseaux. La deuxième colonne...*» Soudain, l'elfe est appelé pour aider quelqu'un à monter sa tente.

Vous vous dites que la deuxième colonne doit être ce que vous allez jouer en réponse : X pour Pierre, Y pour Papier et Z pour Ciseaux. Gagner à chaque fois serait suspect, les réponses doivent donc être soigneusement choisies.

Le vainqueur du tournoi est le joueur qui obtient le score le plus élevé. Votre score total est la somme de vos scores pour chaque tour. Le score d'un tour est le score de la forme choisie (1 pour la pierre, 2 pour le papier et 3 pour les ciseaux) plus le score du résultat du tour (0 si vous avez perdu, 3 si le tour a été nul et 6 si vous avez gagné).

Comme vous ne pouvez pas savoir si l'elfe essaie de vous aider ou de vous piéger, vous devez calculer le score que vous obtiendriez si vous suiviez le guide de stratégie.

Supposons, par exemple, que l'on vous donne le guide stratégique suivant :
```txt
A Y
B X
C Z
```

Ce guide stratégique prédit et recommande ce qui suit :

- Au premier tour, votre adversaire choisira la Pierre (A), et vous devriez choisir le Papier (Y). Cela se termine par une victoire pour vous avec un score de 8 (2 parce que vous avez choisi le papier + 6 parce que vous avez gagné).
- Au deuxième tour, votre adversaire choisira le papier (B), et vous devrez choisir la pierre (X). Vous perdez donc avec un score de 1 (1 + 0).
- Le troisième tour est un match nul, les deux joueurs choisissant Ciseaux, ce qui vous donne un score de 3 + 3 = 6.

Dans cet exemple, si vous suiviez le guide stratégique, vous obtiendriez un score total de 15 (8 + 1 + 6).

Quel serait votre score total si tout se déroulait exactement selon votre guide stratégique ?

## Seconde partie

L'elfe finit d'aider à monter la tente et revient furtivement vers vous. «*Quoi qu'il en soit, la deuxième colonne indique comment le round doit se terminer : X signifie que vous devez perdre, Y signifie que vous devez faire match nul et Z signifie que vous devez gagner. Bonne chance !*»

Le score total est toujours calculé de la même manière, mais vous devez maintenant déterminer quelle forme choisir pour que la manche se termine comme indiqué. L'exemple ci-dessus se présente maintenant comme suit :

    Au premier tour, votre adversaire choisira le rocher (A), et vous avez besoin que le tour se termine par un match nul (Y), donc vous choisissez également le rocher. Cela vous donne un score de 1 + 3 = 4.
    Au deuxième tour, votre adversaire choisira le papier (B), et vous choisirez le rocher, ce qui vous fera perdre (X) avec un score de 1 + 0 = 1.
    Au troisième tour, vous vaincrez les Ciseaux de votre adversaire avec la Pierre pour un score de 1 + 6 = 7.

Maintenant que vous avez correctement décrypté le guide stratégique ultra top secret, vous obtenez un score total de 12.

En suivant les instructions de l'Elfe pour la deuxième colonne, quel serait votre score total si tout se déroulait exactement selon votre guide stratégique ?
