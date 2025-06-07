import functools
from math import prod
from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # seconde
        return result
    return _timer


class TobogganTrajectory:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.slope_grid: list = self._extract_datas()
        self.every_move: tuple = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
        self.list_tree_counter: list = []
        self.tree_counter: int = 0
 
    @timer
    def display_result(self) -> None:
        self._every_move()
        print(f"Nombre d'arbres rencontrés pour le mouvement d3, b1 : {self.list_tree_counter[1]}")
        print(f"Produit de l'ensemble des nombres d'arbres pour chaque pente : {prod(self.list_tree_counter)}")

    def _extract_datas(self) -> list:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            return [line[:-1] for line in f]

    def _every_move(self):
        for coord in self.every_move:
            self._move(coord)
            self.list_tree_counter.append(self.tree_counter)

    def _move(self, coord: tuple[int, int]) -> None:
        self.tree_counter = 0
        x, y = 0, 0
        while y < len(self.slope_grid):
            line = self.slope_grid[y]
            self._tree_counter(line, x)
            x += coord[0]
            if x >= len(line):
                x = x % len(line)
            y += coord[1]

    def _tree_counter(self, line: str, x: int) -> None:
        if line[x] == "#":
            self.tree_counter += 1


if __name__ == "__main__":
    TobogganTrajectory(DATAS_FILE).display_result()
