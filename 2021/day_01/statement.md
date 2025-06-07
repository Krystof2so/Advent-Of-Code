# Balayage du sonar

## Première partie

Vous êtes en train de vaquer à vos occupations sur un navire en mer lorsque l'alarme de l'engin à la mer se déclenche ! Vous vous précipitez pour voir si vous pouvez aider. Apparemment, l'un des elfes a trébuché et a accidentellement envoyé les clés du traîneau dans l'océan !

En un rien de temps, vous vous retrouvez à l'intérieur d'un sous-marin que les lutins gardent prêt à affronter ce genre de situation. Il est recouvert de guirlandes de Noël (parce que c'est normal), et il est même équipé d'une antenne expérimentale qui devrait permettre de retrouver les clés si vous parvenez à augmenter suffisamment la puissance de son signal. Un petit compteur indique la puissance du signal de l'antenne en affichant de 0 à 50 étoiles.

Votre instinct vous dit que pour sauver Noël, vous devez obtenir les cinquante étoiles avant le 25 décembre.

Récupérez des étoiles en résolvant des énigmes. Deux énigmes seront disponibles chaque jour du calendrier de l'Avent ; la deuxième énigme sera débloquée lorsque vous aurez terminé la première. Chaque énigme donne droit à une étoile. Bonne chance !

Lorsque le sous-marin descend sous la surface de l'océan, il effectue automatiquement un balayage sonar du fond marin à proximité. Sur un petit écran, le rapport de balayage sonar (votre entrée d'énigme) apparaît : chaque ligne est une mesure de la profondeur du fond marin au fur et à mesure que le balayage s'éloigne du sous-marin.

Par exemple, supposons que vous ayez le rapport suivant :

```txt
200
208
210
200
207
240
269
260
263
```

Ce rapport indique que, en balayant vers l'extérieur à partir du sous-marin, le sonar a trouvé des profondeurs de 199, 200, 208, 210, et ainsi de suite.

La première chose à faire est de déterminer la vitesse à laquelle la profondeur augmente, afin de savoir à quoi on a affaire - on ne sait jamais si les clés vont être emportées dans des eaux plus profondes par un courant océanique, un poisson ou autre chose.

Pour ce faire, comptez le nombre de fois qu'une mesure de profondeur augmente par rapport à la mesure précédente. (Il n'y a pas de mesure avant la première mesure.) Dans l'exemple ci-dessus, les changements sont les suivants :

```txt
199 (N/A - pas de mesure antérieure)
200 (augmentation)
208 (augmentation)
210 (augmentation)
200 (diminution)
207 (augmentation)
240 (augmentation)
269 (augmentation)
260 (diminution)
263 (augmentation)
```

Dans cet exemple, 7 mesures sont plus grandes que la précédente.

Combien de mesures sont plus grandes que la mesure précédente ?

## Seconde partie

La prise en compte de chaque mesure n'est pas aussi utile que vous le pensiez : il y a trop de bruit dans les données.

Au lieu de cela, considérez les sommes d'une fenêtre coulissante de trois mesures. Reprenons l'exemple ci-dessus :

```txt
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
```

Commencez par comparer la première et la deuxième fenêtre de trois mesures. Les mesures de la première fenêtre sont marquées A (199, 200, 208) ; leur somme est 199 + 200 + 208 = 607. La deuxième fenêtre est marquée B (200, 208, 210) ; sa somme est de 618. La somme des mesures de la deuxième fenêtre est plus grande que la somme de la première, de sorte que cette première comparaison a augmenté.

Votre objectif est maintenant de compter le nombre de fois où la somme des mesures dans cette fenêtre coulissante augmente par rapport à la somme précédente. Ainsi, comparez A avec B, puis comparez B avec C, puis C avec D, et ainsi de suite. Arrêtez-vous lorsqu'il ne reste plus assez de mesures pour créer une nouvelle somme de trois mesures.

Dans l'exemple ci-dessus, la somme de chaque fenêtre de trois mesures est la suivante :

```txt
A : 607 (N/A - pas de montant précédent)
B : 618 (augmentation)
C : 618 (pas de changement)
D : 617 (diminution)
E : 647 (augmentation)
F : 716 (augmentation)
G : 769 (augmentation)
H : 792 (augmentation)
```

Dans cet exemple, il y a 5 sommes qui sont plus grandes que la somme précédente.

Considérons les sommes d'une fenêtre coulissante à trois mesures. Combien de sommes sont plus grandes que la somme précédente ?

