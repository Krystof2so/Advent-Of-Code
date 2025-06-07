import functools    
from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0.002 seconde
        return result
    return _timer


class ThreeSides:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.all_datas: list[list[int]] = self._extract_datas()

    @timer
    def display_result(self):
        print(
            f"Nombre de triangles valides (données horizontales) : {self._horizontal_data()}\n"
            f"Nombre de triangles valides (données verticales) : {self._vertical_data()}"
        )

    def _extract_datas(self) -> list[list[int]]:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            data_list = [list(map(int, line.strip().split())) for line in f]
        return data_list

    def _horizontal_data(self):
        return self._valid_triangles(self.all_datas)

    def _vertical_data(self) -> int:
        """Réorganiser les données avant de vérifier la validité de chaque triangle."""
        # Réorganiser les données verticalement :
        vertical_data_list = [list(col) for col in list(zip(*self.all_datas))]
        # Aplcnir la liste des donnée verticales en une seule liste :
        flattened_data = [item for sublist in vertical_data_list for item in sublist]
        # Créer des tuples de trois éléments à partir de la liste aplanie :
        all_news_triangles = [list(flattened_data[i:i+3]) for i in range(0, len(flattened_data), 3)]
        return self._valid_triangles(all_news_triangles)

    @staticmethod
    def _valid_triangles(list_triangles) -> int:
        """
        Pour vérifier la validité d'un triangle, il est nécessaire que la somme des longueurs
        des deux côtés les plus courts soit supérieure à la longueur du plus long côté 
        (théorème de l'inégalité triangulaire), soit c1 + c2 > c3. Cela peut également se 
        simplifier de la façon suivante : a + b + c > 2c (somme des troix côtés supérieure à 
        longueur du côté le plus grand multipliée par 2), car c'est équivalent à :
        - a + b + c -2c > 0
        - a + b > c.
        """
        return sum(1 for triangle in list_triangles if sum(triangle) > 2 * max(triangle))

    
if __name__ == "__main__":
    ThreeSides(DATAS_FILE).display_result()
