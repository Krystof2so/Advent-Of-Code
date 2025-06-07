from os import path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class TitleClass:

    def __init__(self, file: str):
        self.all_datas: list[int] = self._extract_datas(file)
        self.start_frequency: int = 0

    def __str__(self):
        return f"Fréquence = {sum(self.all_datas)}\nPremière fréquence double = {self.frequency_of_reach_twice()}"

    @staticmethod
    def _extract_datas(file: str) -> list[int]:
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            return [int(line.strip()) for line in f if line.strip()]

    def frequency_of_reach_twice(self) -> int:
        seen_frequencies: set[int] = set()  # L'ensemble permet de vérifier rapidement la orésence de doublons
        current_frequency = self.start_frequency
        while True:  # parcourt indéfinimentr jusqu'à trouver un doucblon
            for change in self.all_datas:
                if current_frequency in seen_frequencies:
                    return current_frequency
                seen_frequencies.add(current_frequency)
                current_frequency += change


if __name__ == "__main__":
    start_time = perf_counter()
    print(TitleClass(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time}")
