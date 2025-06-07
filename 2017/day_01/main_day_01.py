from os import path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class Captcha:

    def __init__(self, file: str):
        self.all_datas = self._extract_datas(file)

    def __str__(self):
        return (f"Solution du captcha N°1 : {self._sum_in_circular_list()}\n"
                f"Solution du captcha N°2 : {self._sum2_in_circular_list()}")

    @staticmethod
    def _extract_datas(file):
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            return [int(char) for char in f.read().strip() if char.isdigit()]

    def _sum_in_circular_list(self):
        return (sum(n for i, n in enumerate(self.all_datas[:-1]) if self.all_datas[i] == self.all_datas[i + 1])
                + self.all_datas[0] if self.all_datas[0] == self.all_datas[-1] else 0)

    def _sum2_in_circular_list(self):
        len_datas = len(self.all_datas)
        return sum(n for i, n in enumerate(self.all_datas) if n == self.all_datas[(i + len_datas // 2) % len_datas])


if __name__ == "__main__":
    start_time = perf_counter()
    print(Captcha(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time} seconde")  # 0.001
