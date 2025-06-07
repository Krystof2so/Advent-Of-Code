# Jour 2 : Sécurité des toilettes

## Première partie

Vous arrivez au quartier général du lapin de Pâques à la faveur de l'obscurité. Mais vous êtes parti si vite que vous avez oublié d'aller aux toilettes ! Les salles de bains des immeubles de bureaux chics comme celui-ci sont généralement équipées de serrures à clavier, et vous cherchez le code à la réception.

Vous cherchez donc le code à l'accueil. « *Afin d'améliorer la sécurité* », dit le document que vous trouvez, « *les codes des salles de bains ne seront plus notés. Veuillez donc mémoriser et suivre la procédure ci-dessous pour accéder aux salles de bains* ».

Le document explique ensuite que chaque bouton à presser peut être trouvé en commençant par le bouton précédent et en se déplaçant vers les boutons adjacents sur le clavier : U se déplace vers le haut, D se déplace vers le bas, L se déplace vers la gauche et R se déplace vers la droite. Chaque ligne d'instructions correspond à une touche, en commençant par la touche précédente (ou, pour la première ligne, la touche « 5 ») ; appuyez sur la touche sur laquelle vous vous trouvez à la fin de chaque ligne. Si un mouvement ne mène pas à un bouton, ignorez-le.

Comme vous ne pouvez pas vous retenir plus longtemps, vous décidez de trouver le code en vous rendant à la salle de bains. Vous imaginez un clavier comme celui-ci :
```txt
1 2 3
4 5 6
7 8 9
```

Supposons que vos instructions soient les suivantes :
```txt
ULL
RRDDD
LURDL
UUUUD
```

- Vous commencez à « 5 » et vous vous déplacez vers le haut (jusqu'à « 2 »), vers la gauche (jusqu'à « 1 »), et vers la gauche (vous ne pouvez pas, et vous restez sur « 1 »), donc le premier bouton est 1.
- En partant du bouton précédent (« 1 »), vous vous déplacez deux fois vers la droite (jusqu'à « 3 »), puis trois fois vers le bas (en vous arrêtant à « 9 » après deux déplacements et en ignorant le troisième), ce qui vous donne le chiffre 9.
- En continuant à partir de « 9 », vous vous déplacez vers la gauche, le haut, la droite, le bas et la gauche, ce qui vous amène à 8.
- Enfin, vous vous déplacez quatre fois vers le haut (en vous arrêtant à « 2 »), puis une fois vers le bas, ce qui donne 5.

Ainsi, dans cet exemple, le code de la salle de bains est 1985.

Les instructions du document que vous avez trouvé à la réception constituent l'entrée de votre énigme. Quel est le code des toilettes ?

## Seconde partie

Vous arrivez enfin à la salle de bains (elle se trouve à plusieurs minutes de marche du hall d'entrée, ce qui permet aux visiteurs de voir les nombreuses salles de conférence et fontaines à eau de cet étage) et vous allez composer le code. À la grande consternation de votre vessie, le clavier n'est pas du tout comme vous l'aviez imaginé. Au contraire, vous êtes confronté au résultat de centaines d'heures de réunions de conception de claviers de salle de bains :

```text
    1
  2 3 4
5 6 7 8 9
  A B C
    D
```

Vous commencez toujours à « 5 » et vous vous arrêtez lorsque vous êtes sur un bord, mais si l'on vous donne les mêmes instructions que ci-dessus, le résultat est très différent :

- Vous commencez à « 5 » et ne bougez pas du tout (vers le haut et la gauche sont tous deux des bords), et vous terminez à « 5 ».
- En continuant à partir de « 5 », vous vous déplacez deux fois vers la droite et trois fois vers le bas (en passant par « 6 », « 7 », « B », « D », « D »), ce qui vous amène à « D ».
- Puis, à partir de « D », vous vous déplacez encore cinq fois (en passant par « D », « B », « C », « C », « B »), pour arriver à B.
- Enfin, après cinq autres déplacements, vous arrivez à 3.

Ainsi, compte tenu de la disposition actuelle du clavier, le code serait 5DB3.

En utilisant les mêmes instructions dans votre puzzle, quel est le code correct pour la salle de bains ?

