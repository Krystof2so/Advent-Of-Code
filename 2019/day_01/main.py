from os import path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class CompleteFuel:

    def __init__(self, file: str):
        self.all_datas = self._extract_datas(file)

    def __str__(self):
        return (f"Total du carburant pour les modules : {sum(mass // 3 - 2 for mass in self.all_datas)} litres.\n"
                f"Total carburant au total (masse carburant comprise) : "
                f"{sum(self._fuel_for_mass(mass) for mass in self.all_datas)} litres.")

    @staticmethod
    def _extract_datas(file: str) -> list[int]:
        full_path = path.join(path.dirname(__file__), file)
        with open(full_path, "r", encoding="utf-8") as f:
            return [int(line.strip()) for line in f if line.strip()]
    
    @staticmethod
    def _fuel_for_mass(mass: int) -> int
        """Calcule le carburant nécessaire pour un module donné, y compris le carburant supplémentaire requis."""
        fuel = 0
        while (mass := mass // 3 - 2) > 0:  # Utilisation de l'opérateur walrus 
            fuel += mass
        return fuel

   
if __name__ == "__main__":
    start_time = perf_counter()
    print(CompleteFuel(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time} seconde")  # 0.0003
