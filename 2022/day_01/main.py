from heapq import nlargest  # Pour extraire efficacement les plus grandes valeurs
from os import path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class CalorieCount:

    def __init__(self, file: str):
        self.all_datas: list[list[int]] = self._extract_datas(file)
        # nlargest(k, iterable) : retourne les k valeurs les plus grandes de l'itérable
        self.three_lutins_more_charged: list[int] = nlargest(3, (sum(charge) for charge in self.all_datas))

    def __str__(self):
        return (f"Calories maximum portées par un lutin : {max(self.three_lutins_more_charged)}\n"
                f"Total des calories portées par les trois lutins qui en portent le plus : " 
                f"{sum(self.three_lutins_more_charged)}")

    @staticmethod
    def _extract_datas(file: str) -> list[list[int]]:
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            groups: list[list[int]] = []
            current_group: list[int] = []
            for line in f:
                stripped_line: str = line.strip()
                if stripped_line:  # Si la ligne n'est pas vide
                    current_group.append(int(stripped_line))
                elif current_group:  # Si la ligne est vide et qu'on a un groupe en cours
                    groups.append(current_group)
                    current_group = []
            if current_group:  # Ajouter le dernier groupe s'il existe
                groups.append(current_group)
        return groups


if __name__ == "__main__":
    start_time = perf_counter()
    print(CalorieCount(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0.0006 seconde
