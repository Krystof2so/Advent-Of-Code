# Système de gestion des stocks 

## Première partie

Vous arrêtez votre chute dans le temps, reprenez votre souffle et consultez l'écran de l'appareil. « *Destination atteinte. Année en cours : 1518. Lieu actuel : Placard utilitaire du Pôle Nord 83N10*. » Vous avez réussi ! Maintenant, il faut trouver ces anomalies.

À l'extérieur de l'armoire, vous entendez des pas et une voix. « ...*Je n'en suis pas sûr non plus. Mais maintenant que tant de gens ont des cheminées, peut-être qu'il pourrait se faufiler par là ?* » Une autre voix répond : « *En fait, nous travaillons sur un nouveau type de costume qui lui permettrait de se faufiler dans des espaces aussi étroits. Mais j'ai entendu dire qu'il y a quelques jours, ils ont perdu le tissu du prototype, les plans de conception, tout ! Personne dans l'équipe ne semble se souvenir des détails importants du projet !* »

« *N'auraient-ils pas eu assez de tissu pour remplir plusieurs cartons dans l'entrepôt ? Ils auraient été stockés ensemble, donc les identifiants des cartons devraient être similaires. Dommage qu'il faille une éternité pour rechercher deux boîtes similaires dans l'entrepôt*... » Ils s'éloignent trop pour en entendre davantage.

Tard dans la nuit, vous vous faufilez jusqu'à l'entrepôt - qui sait quels paradoxes vous pourriez provoquer si vous étiez découvert - et vous utilisez votre appareil au poignet pour scanner rapidement chaque boîte et produire une liste des candidats probables (votre puzzle).

Pour vous assurer que vous n'en avez pas oublié, vous scannez à nouveau les boîtes des candidats probables, en comptant le nombre de celles dont l'ID contient exactement deux lettres, puis en comptant séparément celles dont l'ID contient exactement trois lettres. Vous pouvez multiplier ces deux nombres pour obtenir une somme de [contrôle rudimentaire](https://fr.wikipedia.org/wiki/Somme_de_contr%C3%B4le) et la comparer à ce que votre appareil prédit.

Par exemple, si vous voyez les ID de boîte suivants :

- abcdef ne contient aucune lettre apparaissant exactement deux ou trois fois.
- bababc contient deux a et trois b, et compte donc pour les deux.
- abbcde contient deux b, mais aucune lettre n'apparaît exactement trois fois.
- abcccd contient trois c, mais aucune lettre n'apparaît exactement deux fois.
- aabcdd contient deux a et deux d, mais il ne compte qu'une fois.
- abcdee contient deux e.
- ababab contient trois a et trois b, mais il ne compte qu'une fois.

Parmi ces identifiants, quatre contiennent une lettre qui apparaît exactement deux fois et trois contiennent une lettre qui apparaît exactement trois fois. En multipliant ces chiffres, on obtient une somme de contrôle de 4 * 3 = 12.

Quelle est la somme de contrôle de votre liste d'identifiants de boîtes ?

## Seconde partie

Confiant dans le fait que votre liste d'identifiants de boîtes est complète, vous êtes prêt à trouver les boîtes remplies de prototypes de tissus.

Les boîtes auront des identifiants qui diffèrent d'exactement un caractère à la même position dans les deux chaînes. Par exemple, étant donné les identifiants de boîtes suivants :
```txt
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
```

Les identifiants abcde et axcye sont proches, mais ils diffèrent par deux caractères (le deuxième et le quatrième). En revanche, les identifiants fghij et fguij diffèrent d'un seul caractère, le troisième (h et u). Il doit s'agir des bonnes boîtes.

Quelles sont les lettres communes aux deux boîtes correctes ? (Dans l'exemple ci-dessus, on trouve cela en supprimant le caractère différent de l'un des deux identifiants, ce qui donne fgij).
