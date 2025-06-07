from itertools import combinations
from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class Checksum:

    def __init__(self, puzzle: str):
        self.puzzle = puzzle
        self.all_datas: list[list[int]] = self._extract_datas()

    def __str__(self):
        return (f"Somme de contrôle de la feuille de calcul = {self._checksum_value_calculation()}\n"
                f"Somme de contrôle par divisions = {self._checksum_value_division()}")

    def _extract_datas(self) -> list[list[int]]:
        full_path = Path(__file__).parent / self.puzzle
        with open(full_path, "r", encoding="utf-8") as f:
            return [[int(num) for num in line.split()] for line in f if line.strip()]

    def _checksum_value_calculation(self):
        return sum([max(values) - min(values) for values in self.all_datas])

    def _checksum_value_division(self):
        """Chaque liste (ligne) de nombres est triée dans un ordre décroissant, avant de combiner des paires.
        Dès qu'une paire valide (dont la division n'a pas de reste) est trouvée ('next'), 
        le quotient est calculé et ajouté à l'itérable, et on passe à la ligne de nombres suivante.
        La fonction retourne ensuite la somme des nombres contenus dans l'itérable."""
        return sum(
        next(a // b for a, b in combinations(sorted(values, reverse=True), 2) if a % b == 0) for values in self.all_datas
        )


if __name__ == "__main__":
    start_time = perf_counter()
    print(Checksum(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.5f} seconde")  # 0.0005 seconde
