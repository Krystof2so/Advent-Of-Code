# Advent Of Code 2024 - Day 1

from collections import Counter
from os import path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class Day01:

    def __init__(self, file: str):
        self.file = file
        self.left_list, self.right_list = self._create_lists()

    def __str__(self):
        return (f"Distance totale entre les deux listes : {self._distance_between_lists()}\n"
                f"Score de similarité : {self._similarity_score()}")

    def _create_lists(self) -> tuple[list[int], list[int]]:
        full_path = path.join(path.dirname(__file__), self.file)
        with open(full_path, "r", encoding="utf-8") as f:
            left_list, right_list = zip(*(map(int, line.strip().split()) for line in f))
        return list(left_list), list(right_list)

    def _distance_between_lists(self) -> int:
        return sum([abs(sorted(self.left_list)[i] - sorted(self.right_list)[i]) for i in range(len(self.left_list))])

    def _similarity_score(self) -> int:
        return sum(number * Counter(self.right_list)[number] for number in set(self.left_list) & set(self.right_list))


if __name__ == "__main__":
    start_time = perf_counter()
    print(Day01(DATAS_FILE))
    print(f"Temps d'exécution: {perf_counter() - start_time}")  # 0.24
