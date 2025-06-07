from os import path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class SonarSweep:

    def __init__(self, file: str):
        self.all_datas: list[int] = self._extract_datas(file)

    def __str__(self):
        return (f"Nombre de mesures plus grandes que la précedente : {self._count_larger_measures(self.all_datas)}\n"
                f"Nombre de mesures (regroupées par trois) plus grandes que la précédente : " 
                f"{self._count_larger_3_measures()}")

    @staticmethod
    def _extract_datas(file: str) -> list[int]:
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            return [int(line.strip()) for line in f if line.strip()]

    @staticmethod
    def _count_larger_measures(measures: list[int]) -> int:
        """Compte les éléments d'une liste qui sont plus grands que leur précédent."""
        return sum(curr > prev for prev, curr in zip(measures, measures[1:]))
    
    def _count_larger_3_measures(self) -> int:
        """Compte les sommes des groupes de trois mesures plus grandes que les précédentes."""
        grouped_sums = [sum(self.all_datas[i:i + 3]) for i in range(len(self.all_datas) - 2)]
        return self._count_larger_measures(grouped_sums)


if __name__ == "__main__":
    start_time = perf_counter()
    print(SonarSweep(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0,0016  
