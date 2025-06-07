from itertools import combinations
from math import prod
from os import path
from time import perf_counter
from typing import Optional

DATAS_FILE = "puzzle.txt"


class ReportRepair:

    def __init__(self, file: str):
        self.all_datas = self._extract_datas(file)

    def __str__(self):
        return (
            f"Le produit des deux entrées dont la somme est égale à 2020 est : {self._tuple_product(2)}\n"
            f"Le produit des trois entrées dont la somme est égale à 2020 est : {self._tuple_product(3)}"
        )

    @staticmethod
    def _extract_datas(file: str) -> list[int]:
        """Lit le fichier et extrait une liste d'entiers."""
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            return [int(line.strip()) for line in f if line.strip()]

    def _tuple_product(self, combination_size: int) -> Optional[int]:
        """Trouve le produit des nombres dont la somme est égale à 2020, en fonction de la taille des combinaisons."""
        for combination in combinations(self.all_datas, combination_size):
            return prod(combination) if sum(combination) == 2020 else None


if __name__ == "__main__":
    start_time = perf_counter()
    print(ReportRepair(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time} seconde")  # 0.032
