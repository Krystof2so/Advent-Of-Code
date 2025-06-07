# Jour 2 : On m'a dit qu'il n'y aurait pas de maths

## Première partie

Les lutins sont à court de papier d'emballage et doivent donc passer une commande pour en obtenir davantage. Ils ont une liste des dimensions (longueur l, largeur w, et hauteur h) de chaque cadeau, et ne veulent commander que la quantité exacte dont ils ont besoin.

Heureusement, chaque cadeau est une boîte (un prisme rectangulaire droit parfait), ce qui facilite le calcul du papier d'emballage nécessaire pour chaque cadeau : trouver la surface de la boîte, qui est 2 x l x w + 2 x w xh + 2 x h x l. Les lutins ont également besoin d'un peu de papier supplémentaire pour chaque cadeau : la surface du plus petit côté.

Par exemple, 
- Un cadeau de dimensions 2x3x4 nécessite 2x6 + 2x12 + 2x8 = 52 pieds carrés de papier d'emballage plus 6 pieds carrés de marge, pour un total de 58 pieds carrés.
- Un cadeau de dimensions 1x1x10 nécessite 2x1 + 2x10 + 2x10 = 42 pieds carrés de papier d'emballage plus 1 pied carré de jeu, pour un total de 43 pieds carrés.

Tous les nombres de la liste des lutins sont exprimés en pieds. Combien de mètres carrés de papier d'emballage doivent-ils commander ?

## Seconde partie

Les lutins manquent également de ruban. Les rubans étant tous de la même largeur, ils n'ont qu'à se préoccuper de la longueur à commander, qu'ils souhaitent encore une fois exacte.

Le ruban nécessaire pour emballer un cadeau correspond à la distance la plus courte autour de ses côtés, ou au plus petit périmètre d'une face. Chaque cadeau a également besoin d'un nœud fait de ruban ; le nombre de pieds de ruban requis pour un nœud parfait est égal au volume en pieds cubes du cadeau. Ne leur demandez pas comment ils font le nœud, ils ne vous le diront jamais.

Par exemple :
- Un cadeau de dimensions 2x3x4 nécessite 2+2+3+3 = 10 pieds de ruban pour envelopper le cadeau, plus 2*3*4 = 24 pieds de ruban pour le nœud, soit un total de 34 pieds.
- Un cadeau aux dimensions 1x1x10 nécessite 1+1+1+1 = 4 pieds de ruban pour envelopper le cadeau plus 1*1*10 = 10 pieds de ruban pour le nœud, soit un total de 14 pieds.

Combien de mètres de ruban doivent-ils commander au total ?
