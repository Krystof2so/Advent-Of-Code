import functools
from time import perf_counter


def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # seconde
        return result
    return _timer


class SpiralMemory:

    def __init__(self, puzzle: int) -> None:
        self.puzzle: int = puzzle
        self.x, self.y = 0, 0  # Coordonnées x, y de départ
        self.segment: int = 1  # Longueur initiale du segment
        self.value: int = 1  # Valeur initiale (Coordonnées 0, 0)
        self.count_segment: int = 0  # Compteur de segment
        self.grid = {(0, 0): 1}  # Grille avec la valeur initiale
        # Tableau des directions : droite, haut, gauche, bas :
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    @timer
    def display_result(self) -> None:
        #print(f"Nombre de pas requis : {self._manhattan_distance()}")
        print(f"Première valeur supérieure à {self.puzzle} : {self._spiral_memory()}")

    def _manhattan_distance(self) -> int:
        self._spiral_memory()
        return abs(self.x) + abs(self.y)

    """def _spiral_memory(self) -> None:
        dx, dy = self.directions[0]  # Commencer par se déplacer vers la droite
        while self.value < self.puzzle:
            for _ in range(self.segment):
                self.x += dx
                self.y += dy
                self.value += 1
                if self.value == self.puzzle:
                    return  # Sortir de la boucle si la valeur cible est atteinte
            # Changer de direction :
            self.count_segment += 1
            if self.count_segment % 2 == 0:
                self.segment += 1  # Augmenter la longueur du segment tous les deux segments

            dx, dy = self.directions[self.count_segment % 4]"""

    def _spiral_memory(self) -> int:
        dx, dy = self.directions[0]  # Commencer par se déplacer vers la droite
        while True:
            for _ in range(self.segment):
                self.x += dx
                self.y += dy
                # Calculer la somme des valeurs adjacentes
                new_value = sum(self.grid.get((self.x + i, self.y + j), 0) for i in (-1, 0, 1) for j in (-1, 0, 1))
                # Mettre à jour la grille avec la nouvelle valeur
                self.grid[(self.x, self.y)] = new_value
                # Vérifier si la valeur est supérieure à l'entrée
                if self.value > self.puzzle:
                    return new_value
            # Changer de direction :
            self.count_segment += 1
            if self.count_segment % 2 == 0:
                self.segment += 1  # Augmenter la longueur du segment tous les deux segments
            dx, dy = self.directions[self.count_segment % 4]


if __name__ == "__main__":
    SpiralMemory(361527).display_result()
