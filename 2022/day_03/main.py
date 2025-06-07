import functools
from pathlib import Path
from string import ascii_letters
from time import perf_counter

DATAS_FILE = "puzzle.txt"

def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0.001538 seconde
        return result
    return _timer


class RucksackReorganization:

    def __init__(self) -> None:
        self.all_datas: list[str] = self._extract_datas() 
        self.priority_dict: dict = {letter: index  for index, letter in enumerate(ascii_letters, 1)}

    @timer
    def display_result(self) -> None:
        print(f"Somme de priorité des objets : {self._part1()}\n"
              f"Somme de priorité des bagdes des groupes des elfes : {self._part2()}")

    def _extract_datas(self) -> list:
        with (Path(__file__).parent / DATAS_FILE).open("r", encoding="utf-8") as f:
            list_datas = [line.strip() for line in f]
        return list_datas

    def _part1(self) -> int:
        """Calcul de la somme des priorités à l'aide d'une compréhension de liste."""
        return sum(self._get_priority(self._find_common_item(rucksack)) for rucksack in self.all_datas)

    def _part2(self) -> int:
        """Calcul de la somme des priorités des badges."""
        return sum(self._get_priority(self._find_common_badge(elfe_group)) for elfe_group in self._elfe_groups())

    def _find_common_item(self, rucksack: str) -> str:
        """Trouver l'objet commun aux deux compartiments du sac à dos."""
        middle = len(rucksack) // 2
        compartment1, compartment2 = set(rucksack[:middle]), set(rucksack[middle:])
        return compartment1.intersection(compartment2).pop()  # Rettounr l'objet commun (unique)
    
    def _find_common_badge(self, elfe_group: tuple[set, set, set]) -> str:
        """Trouver le badge commun pour le groupe des trois elfes."""
        common_badge = elfe_group[0] & elfe_group[1] & elfe_group[2]
        return common_badge.pop()

    def _elfe_groups(self) -> list[tuple[set, set, set]]:
        """Permet d'obtenir une liste des groupes d'elfes (3 elfes)."""
        return [(set(self.all_datas[i]), set(self.all_datas[i+1]), set(self.all_datas[i+2])) for i in range(0, len(self.all_datas), 3)]

    def _get_priority(self, item: str) -> int:
        """Retourne la priorité d'un objet à l'aide du dictionnaire créé dans le constructeur."""
        return self.priority_dict[item]


if __name__ == "__main__":
    RucksackReorganization().display_result()
