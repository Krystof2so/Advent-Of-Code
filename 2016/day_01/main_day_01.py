"""
Advent Of Code 2016 - Day 1
Pas le temps de prendre un taxi.

Astuce algorithmique avec la distance de Manhattan :
Entre deux points A et B, de coordonnées respectives (xA, yA) et (xB, yB), la distance de Manhattan est définie par :
    d(A, B) = |xB − xA| + |yB − yA|
"""

from os import path
from time import perf_counter

PUZZLE_FILE = "puzzle.txt"


class Travels:

    directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # [Nord, Est, Sud, Ouest]

    def __init__(self, file: str):
        self.instructions: list[str] = self._extract_datas(file)
        self.position: tuple[int, int] = (0, 0)
        self.direction_index: int = 0  # 0 = Nord, 1 = Est, 2 = Sud, 3 = Ouest
        self.positions_traversed = set()
        self.house_rabbit = None

    def __str__(self):
        return f"{self._formatted_result()}"

    @staticmethod
    def _extract_datas(file) -> list[str]:
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            return f.readline().strip().split(', ')

    def _check_positions_traversed(self, dx: int, dy: int, move: int) -> None:
        """Vérifie si la position a déjà été traversée."""
        x, y = self.position
        for _ in range(move):
            x += dx
            y += dy
            if (x, y) in self.positions_traversed:
                self.house_rabbit = (x, y)
                self.positions_traversed = None  # Arrête le suivi pour ne pas surcharger la mémoire
                return
            else:
                self.positions_traversed.add((x, y))

    def _formatted_result(self) -> int:
        return (f"Le QG du lapin de Pâques se trouverait à {self._manhattan_distance()} pâtés de maisons.\n"
                f"Mais selon les dernières instructions il est à {sum(map(abs, self.house_rabbit))} pâtés de maison.")

    def _manhattan_distance(self) -> int:
        """Calcule la distance de Manhattan entre la position initiale et la position finale."""
        for instruction in self.instructions:
            distance = int(instruction[1:])
            self.direction_index = (self.direction_index + (1 if instruction[0] == "R" else -1)) % 4
            dx, dy = Travels.directions[self.direction_index]
            if isinstance(self.positions_traversed, set):
                self._check_positions_traversed(dx, dy, distance)
            self.position = self.position[0] + dx * distance, self.position[1] + dy * distance
        return sum(map(abs, self.position))  # abs() appliqué à chaque élément de self.position à l'aide de map()


if __name__ == "__main__":
    start_time = perf_counter()
    print(Travels(PUZZLE_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time} seconde(s)")  # 0.00095
