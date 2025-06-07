import functools
import re
from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"

def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")
        return result
    return _timer

class FabricCutter:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.all_datas: dict[int, tuple[int, int, int, int]] = self._extract_datas()
        self.grid = {}

    @timer
    def display_result(self) -> None:
        self._mark_claims()
        overlap_count = self._count_overlaps()
        unique_claim_id = self._find_unique_claim()
        print(f"Nombre de pouces carrés de tissu dans deux ou plusieurs revendications : {overlap_count}")
        print(f"Identifiant de la revendication unique : {unique_claim_id}")

    def _extract_datas(self) -> dict[int, tuple[int, int, int, int]]:
        data_dict = {}
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            for line in f:
                match = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
                if match:
                    _id, x, y, width, height = map(int, match.groups())
                    data_dict[_id] = (x, y, width, height)
        return data_dict

    def _mark_claims(self) -> None:
        """Marquer les unités de la grille couvertes par chaque rectangle"""
        for x, y, width, height in self.all_datas.values():
            for i in range(width):
                for j in range(height):
                    coord = (x + i, y + j)
                    if coord in self.grid:
                        self.grid[coord] += 1
                    else:
                        self.grid[coord] = 1

    def _count_overlaps(self) -> int:
        """Compter le nombre d'unités de la grille couvertes par au moins deux rectangles"""
        return sum(1 for count in self.grid.values() if count >= 2)

    def _find_unique_claim(self) -> None | int:
        """Trouver l'identifiant de la revendication unique qui ne chevauche aucune autre revendication"""
        for _id, (x, y, width, height) in self.all_datas.items():
            unique = True
            for i in range(width):
                for j in range(height):
                    coord = (x + i, y + j)
                    if self.grid[coord] > 1:
                        unique = False
                        break
                if not unique:
                    break
            if unique:
                return _id
        return None

if __name__ == "__main__":
    FabricCutter(DATAS_FILE).display_result()

