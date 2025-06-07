from itertools import combinations
from math import prod
from os import path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class TitleClass:

    def __init__(self, file: str):
        self.all_datas: list[list[int]] = self._extract_datas(file)

    def __str__(self):
        return (f"Quantité de papier cadeau nécessaire : {self._giftpaper_quantity()}\n"
                f"Quantité de ruban nécessaire : {self._ribbon_quantity()}")

    @staticmethod
    def _extract_datas(file: str) -> list[list[int]]:
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            return [list(map(int, line.strip().split("x"))) for line in f if line.strip()]

    def _giftpaper_quantity(self) -> int:
        total_paper = 0
        for dim_present in self.all_datas:
            prod_combinations = [2 * prod(comb) for comb in combinations(dim_present, 2)]
            total_paper += sum(prod_combinations) + min(prod_combinations) // 2
        return total_paper

    def _ribbon_quantity(self) -> int:
        total_ribbon = 0
        for dim_present in self.all_datas:
            product = prod(dim_present)
            dim_present.remove(max(dim_present))
            total_ribbon += product + 2 * sum(dim_present)
        return total_ribbon


if __name__ == "__main__":
    start_time = perf_counter()
    print(TitleClass(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0.002
