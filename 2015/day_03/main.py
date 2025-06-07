from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class HousesVisited:

    MOVES = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.all_datas: str = self._extract_datas()

    def __str__(self):
        return (
            f"Nombre de maisons visitées : {self._lonely_santa()}\n"
            f"Nombre de maisons visitées avec Robo_Santa : {self._with_robo_santa()}"
        )

    def _calculate_number_of_houses_visited(self, moves) -> set[tuple[int, int]]:
        x, y = 0, 0
        visited = {(0, 0)}
        for move in moves:
            dx, dy = HousesVisited.MOVES[move]
            x += dx
            y += dy
            visited.add((x, y))
        return visited
                    
    def _extract_datas(self) -> str:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            return f.read().strip()

    def _lonely_santa(self) -> int:
        return len(self._calculate_number_of_houses_visited(self.all_datas))

    def _with_robo_santa(self) -> int:
        houses_visited = {(0, 0)}
        houses_visited.update(self._calculate_number_of_houses_visited(self.all_datas[::2]))
        houses_visited.update(self._calculate_number_of_houses_visited(self.all_datas[1::2]))
        return len(houses_visited)


if __name__ == "__main__":
    start_time = perf_counter()
    print(HousesVisited(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # seconde
