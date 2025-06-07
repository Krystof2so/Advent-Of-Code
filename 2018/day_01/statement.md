# Jour 1 : Calibrage chronologique

## Première partie

"*Nous avons détecté des anomalies temporelles*", vous dit l'un des elfes du Père Noël à la station instrumentale de recherche et de détection des anomalies temporelles. Il avait l'air plutôt inquièt lorsqu'il vous a appelé ici. "*À 500 ans d'intervalle dans le passé, quelqu'un a modifié l'histoire du Père Noël !*"

"*La bonne nouvelle, c'est que les changements ne se propageront pas dans notre flux temporel avant 25 jours, et nous avons un appareil* - il attache quelque chose à votre poignet - *qui vous permettra de corriger les changements sans un tel délai de propagation. Il est configuré pour vous envoyer 500 ans plus loin dans le passé tous les quelques jours ; c'est le mieux que nous ayons pu faire dans un délai aussi court. »

"*La mauvaise nouvelle, c'est que nous détectons une cinquantaine d'anomalies dans le temps ; l'appareil indiquera les anomalies fixées à l'aide d'étoiles. L'autre mauvaise nouvelle, c'est que nous n'avons qu'un seul appareil et que vous êtes la meilleure personne pour ce travail ! Bonne chance...*" Il appuie sur un bouton de l'appareil et vous avez soudain l'impression de tomber. Pour sauver Noël, vous devez récupérer les cinquante étoiles avant le 25 décembre.

Récupérez des étoiles en résolvant des énigmes. Deux puzzles seront disponibles pour chaque jour du calendrier de l'Avent ; le second se débloque lorsque vous avez terminé le premier. Chaque énigme donne droit à une étoile. Bonne chance !

Après avoir eu l'impression de tomber pendant quelques minutes, vous regardez le petit écran de l'appareil. "*Erreur : L'appareil doit être calibré avant la première utilisation. Dérive de fréquence détectée. Impossible de maintenir le verrouillage de la destination.*" Sous le message, l'appareil affiche une séquence de changements de fréquence (l'entrée de votre puzzle). Une valeur comme +6 signifie que la fréquence actuelle augmente de 6 ; une valeur comme -3 signifie que la fréquence actuelle diminue de 3.

Par exemple, si l'appareil affiche des changements de fréquence de +1, -2, +3, +1, en partant d'une fréquence de zéro, les changements suivants se produiront :

    Fréquence actuelle 0, changement de +1 ; fréquence résultante 1.
    Fréquence actuelle 1, changement de -2 ; fréquence résultante -1.
    Fréquence actuelle -1, changement de +3 ; fréquence résultante 2.
    Fréquence actuelle 2, changement de +1 ; fréquence résultante 3.

Dans cet exemple, la fréquence résultante est 3.

Voici d'autres exemples de situations :

    +1, +1, +1 donne 3
    +1, +1, -2 donne 0
    -1, -2, -3 donne -6

En partant d'une fréquence de zéro, quelle est la fréquence résultante après l'application de tous les changements de fréquence ?

## Seconde partie

Vous remarquez que l'appareil répète sans cesse la même liste de changements de fréquence. Pour calibrer l'appareil, vous devez trouver la première fréquence qu'il atteint deux fois.

Par exemple, en utilisant la même liste de changements que ci-dessus, l'appareil fonctionnerait en boucle comme suit :

    Fréquence actuelle 0, changement de +1 ; fréquence résultante 1.
    Fréquence actuelle 1, changement de -2 ; fréquence résultante -1.
    Fréquence actuelle -1, changement de +3 ; fréquence résultante 2.
    Fréquence actuelle 2, changement de +1 ; fréquence résultante 3.
    (A ce stade, l'appareil continue à partir du début de la liste).
    Fréquence actuelle 3, changement de +1 ; fréquence résultante 4.
    Fréquence actuelle 4, changement de -2 ; fréquence résultante 2, qui a déjà été vue.

Dans cet exemple, la première fréquence atteinte deux fois est 2. Notez que votre appareil peut devoir répéter sa liste de changements de fréquence plusieurs fois avant de trouver une fréquence en double, et que des doublons peuvent être trouvés au milieu du traitement de la liste.

Voici d'autres exemples :

    +1, -1 atteint deux fois 0.
    +3, +3, +4, -2, -4 atteint deux fois 10.
    -6, +3, +8, +5, -6 atteint d'abord 5 deux fois.
    +7, +7, -2, -7, -4 atteint d'abord 14 deux fois.

Quelle est la première fréquence que votre appareil atteint deux fois ?

