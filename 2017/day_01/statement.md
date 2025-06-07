# Captcha inversé

## Première partie

La veille de Noël, l'une des elfes du Père Noël vous appelle, paniquée. "*L'imprimante est en panne ! Nous ne pouvons pas imprimer la liste des méchants et des gentils !*" Le temps que vous arriviez au sous-sol 17, il ne reste plus que quelques minutes avant minuit. "*Nous avons un gros problème*", dit- elle ; "*il doit y avoir près de cinquante bogues dans ce système, mais rien d'autre ne peut imprimer la Liste. Placez-vous ici, vite ! On n'a pas le temps d'expliquer ; si vous arrivez à les convaincre de vous payer en étoiles, vous pourrez...*" Elle tire un levier et le monde devient flou.

Lorsque vos yeux peuvent à nouveau faire la mise au point, tout semble beaucoup plus pixelisé qu'auparavant. Elle a dû vous envoyer à l'intérieur de l'ordinateur ! Vous vérifiez l'horloge du système : il reste 25 millisecondes avant minuit. Avec autant de temps, vous devriez pouvoir collecter les cinquante étoiles avant le 25 décembre.

Collectez des étoiles en résolvant des énigmes. Deux énigmes seront disponibles chaque milliseconde du calendrier de l'Avent ; la deuxième énigme sera débloquée lorsque vous aurez terminé la première. Chaque énigme donne droit à une étoile. Bonne chance !

Vous vous trouvez dans une pièce dont l'un des murs porte l'inscription «*digitization quarantine*» (quarantaine de numérisation) sous forme de diodes électroluminescentes. La seule porte est verrouillée, mais elle comporte une petite interface. «*Zone restreinte - Strictement interdit aux utilisateurs numérisés*».

Il est ensuite expliqué que vous ne pouvez quitter le site qu'en résolvant un [captcha](https://fr.wikipedia.org/wiki/CAPTCHA) pour prouver que vous n'êtes pas un humain. Apparemment, vous ne disposez que d'une milliseconde pour résoudre le *captcha* : c'est trop rapide pour un être humain normal, mais en réalité  vous avez l'impression que cela dure des heures.

Le *captcha* vous demande d'examiner une séquence de chiffres (votre entrée de puzzle) et de trouver la somme de tous les chiffres qui correspondent au chiffre suivant dans la liste. La liste étant circulaire, le chiffre qui suit le dernier chiffre est le premier chiffre de la liste.

Par exemple :

- 1122 produit une somme de 3 (1 + 2) parce que le premier chiffre (1) correspond au deuxième chiffre et le troisième chiffre (2) correspond au quatrième chiffre.
- 1111 donne 4 car chaque chiffre (tous les 1) correspond au suivant.
- 1234 produit 0 car aucun chiffre ne correspond au suivant.
- 91212129 produit 9 car le seul chiffre qui correspond au suivant est le dernier chiffre, 9.

Quelle est la solution de votre captcha ?

## Seconde partie

Vous remarquez une barre de progression qui indique que la tâche est terminée à 50 %. Apparemment, la porte n'est pas encore satisfaite, mais elle a émis une étoile en guise d'encouragement. Les instructions changent :

Maintenant, au lieu de considérer le chiffre suivant, il veut que vous considériez le chiffre situé à mi-chemin de la liste circulaire. En d'autres termes, si votre liste contient 10 éléments, n'incluez un chiffre dans votre somme que si le chiffre 10/2 = 5 pas en avant lui correspond. Heureusement, votre liste comporte un nombre pair d'éléments.

Par exemple, 1212 produit 6 : la liste contient 4 éléments et les quatre chiffres correspondent au chiffre situé 2 éléments plus loin :

- 1212 produit 6 : la liste contient 4 éléments, et les quatre chiffres correspondent au chiffre situé 2 éléments plus loin.
- 1221 produit 0, car chaque comparaison se fait entre un 1 et un 2.
- 123425 produit 4, parce que les deux 2 correspondent l'un à l'autre, mais aucun autre chiffre n'a de correspondance.
- 123123 produit 12.
- 12131415 produit 4.

Quelle est la solution à votre nouveau captcha ?