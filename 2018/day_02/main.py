from collections import Counter
from itertools import combinations
from pathlib import Path
from time import perf_counter

PUZZLE = "puzzle.txt"


class InventoryManagement:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.datas: list[str] = self._extract_datas()

    def __str__(self) -> str:
        return (f"Première somme de contrôle = {self._first_checksum()}\n"
                f"Lettres communes aux deux boîtes = {self._find_prototype_boxes()}")

    def _extract_datas(self) -> list[str]:
        full_path = Path(__file__).parent / self.puzzle
        with open(full_path, 'r', encoding="utf-8") as f:
            return [line.strip() for line in f]

    def _find_prototype_boxes(self):
        all_id_pairs = combinations(self.datas, 2)
        for id1, id2 in all_id_pairs:
            # Compter le nombre de différences entre les deux chaînes...
            if sum(c1 != c2 for c1, c2 in zip(id1, id2)) == 1: 
                # ... puis constuire et retourner chaine si une seule différence
                return "".join(c1 for c1, c2 in zip(id1, id2) if c1 == c2)

    def _first_checksum(self) -> int:
        counts = [Counter(package_id).values() for package_id in self.datas]
        return sum(2 in count for count in counts) *  sum(3 in count for count in counts)


if __name__ == "__main__":
   start_time = perf_counter()
   print(InventoryManagement(PUZZLE))
   print(f"Temps d'exécution : {perf_counter() - start_time:.5f} seconde.")
