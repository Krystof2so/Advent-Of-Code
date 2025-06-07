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


class ClassName:

    def __init__(self) -> None:
       self.all_datas = self._extract_datas() 

    @timer
    def display_result(self) -> None:
        print(f"{self.all_datas}")

    def _extract_datas(self) -> list:
        with (Path(__file__).parent / DATAS_FILE).open("r", encoding="utf-8") as f:
            list_datas = [line[:-1] for line in f]
        return list_datas


if __name__ == "__main__":
    ClassName().display_result()
