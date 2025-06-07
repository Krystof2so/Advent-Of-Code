# Jour 2 : Mot de passe Philosophie 

## Première partie

Votre vol part dans quelques jours de l'aéroport de la côte ; le moyen le plus facile de descendre à la côte est le [toboggan](https://fr.wikipedia.org/wiki/Toboggan_(tra%C3%AEneau)).

Le commerçant du magasin de location de toboggans du Pôle Nord passe une mauvaise journée. « *Quelque chose ne va pas avec nos ordinateurs ; nous ne pouvons pas nous connecter !* ". Vous lui demandez si vous pouvez jeter un coup d'œil.

Leur base de données de mots de passe semble être un peu corrompue : certains mots de passe n'auraient pas été autorisés par la politique officielle de l'entreprise de toboggans qui était en vigueur lorsqu'ils ont été choisis.

Pour tenter de résoudre le problème, ils ont créé une liste (votre puzzle) de mots de passe (selon la base de données corrompue) et la politique de l'entreprise au moment où le mot de passe a été défini.

Par exemple, supposons que vous ayez la liste suivante :
```txt
1-3 a : abcde
1-3 b : cdefg
2-9 c : ccccccccc
```

Chaque ligne indique la politique en matière de mots de passe, puis le mot de passe. La politique de mot de passe indique le nombre le plus faible et le plus élevé de fois qu'une lettre donnée doit apparaître pour que le mot de passe soit valide. Par exemple, 1-3 a signifie que le mot de passe doit contenir a au moins 1 fois et au plus 3 fois.

Dans l'exemple ci-dessus, 2 mots de passe sont valables. Le mot de passe du milieu, cdefg, ne l'est pas ; il ne contient aucune occurrence de b, mais doit en contenir au moins une. Le premier et le troisième mots de passe sont valides : ils contiennent un a ou neuf c, tous deux dans les limites de leurs politiques respectives.

Combien de mots de passe sont valides selon leur politique ?

## Seconde partie

Bien qu'il semble que vous ayez validé les mots de passe correctement, ils ne semblent pas correspondre aux attentes du système d'authentification officiel de l'entreprise de toboggans.

Le commerçant se rend soudain compte qu'il vient d'expliquer accidentellement les règles de la politique de mot de passe qu'il appliquait dans son ancien emploi chez le loueur de luges d'en bas de la rue ! La politique officielle de l'entreprise Toboggan fonctionne un peu différemment.

Chaque politique décrit en fait deux positions dans le mot de passe, où 1 signifie le premier caractère, 2 signifie le deuxième caractère, et ainsi de suite. (Attention, les politiques d'entreprise de Toboggan n'ont aucun concept d'« indice zéro » !) Une seule de ces positions doit contenir la lettre donnée. Les autres occurrences de la lettre ne sont pas pertinentes pour l'application de la politique.

Prenons le même exemple de liste que ci-dessus :
```text
1-3 a : abcde est valide : la position 1 contient a et la position 3 n'en contient pas.
1-3 b : cdefg n'est pas valide : ni la position 1 ni la position 3 ne contient b.
2-9 c : ccccccccc n'est pas valide : la position 2 et la position 9 contiennent toutes deux c.
```

Combien de mots de passe sont valides selon la nouvelle interprétation des règles ?
