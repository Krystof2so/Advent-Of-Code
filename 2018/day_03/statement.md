# Quelle que soit la façon dont on le découpe 

## Première partie

Les lutins ont réussi à localiser le prototype de tissu pour le costume du Père Noël (grâce à quelqu'un qui a utilement écrit les numéros de boîtes sur le mur de l'entrepôt au milieu de la nuit). Malheureusement, des anomalies les affectent encore - personne n'arrive même à se mettre d'accord sur la façon de couper le tissu.

La pièce de tissu sur laquelle ils travaillent est un très grand carré, d'au moins 30 cm de côté.

Chaque lutin a fait une réclamation sur la partie du tissu qui serait idéale pour le costume du Père Noël. Toutes les réclamations ont un identifiant et consistent en un rectangle unique dont les bords sont parallèles aux bords du tissu. Le rectangle de chaque réclamation est défini comme suit :

- Le nombre de pouces entre le bord gauche du tissu et le bord gauche du rectangle.
- Le nombre de pouces entre le bord supérieur du tissu et le bord supérieur du rectangle.
- La largeur du rectangle en pouces.
- La hauteur du rectangle en pouces.

Une revendication comme `#123 @ 3,2 : 5x4` signifie que l'ID de revendication 123 spécifie un rectangle situé à 3 pouces du bord gauche, à 2 pouces du bord supérieur, à 5 pouces de large et à 4 pouces de haut. Visuellement, elle revendique les pouces carrés de tissu représentés par `#` (et ignore les pouces carrés de tissu représentés par `.`) dans le diagramme ci-dessous :

```txt
...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
```
Le problème est que de nombreuses revendications se chevauchent, ce qui fait que deux revendications ou plus couvrent une partie des mêmes domaines. Prenons par exemple les revendications suivantes :

- `#1 @ 1,3 : 4x4`
- `#2 @ 3,1 : 4x4`
- `#3 @ 5,5 : 2x2`

D'un point de vue visuel, ils revendiquent les zones suivantes :

```txt
........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
```
Les quatre pouces carrés marqués d'un X sont revendiqués par 1 et 2. (La revendication 3, bien qu'adjacente aux autres, ne chevauche aucune d'entre elles.)

Si les lutins suivent tous leurs propres plans, aucun d'entre eux n'aura assez de tissu. Combien de pouces carrés de tissu se trouvent à l'intérieur de deux revendications ou plus ?


## Seconde partie

Au milieu du chaos, vous remarquez qu'une seule revendication ne recouvre même pas un seul centimètre carré de tissu avec une autre revendication. Si vous parvenez à attirer l'attention sur ce point, les lutins pourront peut-être fabriquer le costume du Père Noël !

Par exemple, dans les revendications ci-dessus, seule la revendication 3 est intacte après que toutes les revendications ont été faites.

Quel est l'identifiant de la seule revendication qui ne se chevauche pas ?

