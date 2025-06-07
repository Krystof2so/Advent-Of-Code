# Plongez ! 

## Première partie

Maintenant, il faut savoir comment piloter cet engin.

Il semble que le sous-marin puisse recevoir une série d'ordres comme avancer de 1, descendre de 2, ou monter de 3 :

- avant (*forward*) X augmente la position horizontale de X unités.
- vers le bas (*down*) X augmente la profondeur de X unités.
- *up* X diminue la profondeur de X unités.

Notez que, puisque vous êtes sur un sous-marin, les commandes vers le bas et vers le haut affectent votre profondeur, et ont donc le résultat inverse de celui auquel on pourrait s'attendre.

Le sous-marin semble avoir déjà une trajectoire planifiée (entrée de votre puzzle). Vous devriez probablement trouver où il va. Par exemple :
```text
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

Votre position horizontale et votre profondeur commencent toutes deux à 0. Les étapes ci-dessus les modifieraient alors comme suit :

- vers l'avant 5 ajoute 5 à votre position horizontale, soit un total de 5.
- vers le bas 5 ajoute 5 à votre profondeur, ce qui donne une valeur de 5.
- avant 8 ajoute 8 à votre position horizontale, soit un total de 13.
- vers le haut 3 diminue votre profondeur de 3, ce qui donne une valeur de 2.
- vers le bas 8 ajoute 8 à votre profondeur, ce qui donne une valeur de 10.
- Avancer de 2 ajoute 2 à votre position horizontale, ce qui donne un total de 15.

Après avoir suivi ces instructions, vous aurez une position horizontale de 15 et une profondeur de 10. (En multipliant ces chiffres, on obtient 150.)

Calculez la position horizontale et la profondeur que vous auriez en suivant le parcours prévu. Qu'obtenez-vous si vous multipliez votre position horizontale finale par votre profondeur finale ?

## Seconde partie

D'après vos calculs, la trajectoire prévue ne semble pas avoir de sens. Vous trouvez le manuel du sous-marin et découvrez que le processus est en fait un peu plus compliqué.

En plus de la position horizontale et de la profondeur, vous devez également suivre une troisième valeur, la visée, qui commence également à 0. Les commandes ont également une signification tout à fait différente de ce que vous pensiez au départ :

    vers le bas X augmente votre visée de X unités.
    vers le haut X diminue votre visée de X unités.
    La commande X vers l'avant a deux effets :
        Elle augmente votre position horizontale de X unités.
        Il augmente votre profondeur de votre visée multipliée par X.

Notez encore une fois que, puisque vous êtes dans un sous-marin, le bas et le haut font le contraire de ce à quoi vous pourriez vous attendre : Le terme « bas » signifie que l'on vise dans la direction positive.

L'exemple ci-dessus a un effet différent :

    En avançant de 5, vous ajoutez 5 à votre position horizontale, soit un total de 5. Comme vous visez 0, votre profondeur ne change pas.
    vers le bas 5 ajoute 5 à votre visée, ce qui donne une valeur de 5.
    vers l'avant 8 ajoute 8 à votre position horizontale, ce qui donne un total de 13. comme votre but est de 5, votre profondeur augmente de 8*5=40.
    vers le haut 3 diminue votre visée de 3, ce qui donne une valeur de 2.
    vers le bas 8 ajoute 8 à votre visée, ce qui donne une valeur de 10.
    2 vers l'avant ajoute 2 à votre position horizontale, soit un total de 15. Comme votre but est de 10, votre profondeur augmente de 2*10=20, soit un total de 60.

Après avoir suivi ces nouvelles instructions, vous aurez une position horizontale de 15 et une profondeur de 60 (en multipliant ces chiffres, on obtient 900).

En utilisant cette nouvelle interprétation des commandes, calculez la position horizontale et la profondeur que vous auriez en suivant la trajectoire prévue. Qu'obtenez-vous si vous multipliez votre position horizontale finale par votre profondeur finale ?
