import functools
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


class CrossedWires:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.wire1_path, self.wire2_path = self._extract_datas()

    @timer
    def display_result(self) -> None:
        print(f"{self.wire1_path}\n{self.wire2_path}")

    def _extract_datas(self) -> tuple[list[str], list[str]]:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            wire1_path = f.readline().strip().split(',')
            wire2_path = f.readline().strip().split(',')
        return wire1_path, wire2_path


if __name__ == "__main__":
    CrossedWires(DATAS_FILE).display_result()
