from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class Dive:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.commands = self._read_commands()
        self.forward_sum, self.down_sum, self.up_sum = self._first_calculation()

    def __str__(self):

        return (f"Premier calcul = {self.forward_sum * (self.down_sum - self.up_sum)}\n"
                f"Second calcul = {self._second_calculation()}")

    def _read_commands(self) -> list[tuple[str, int]]:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            return [(command, int(value)) for line in f for command, value in [line.strip().split()]]

    def _first_calculation(self) -> tuple[int, int, int]:
        forward_sum, down_sum, up_sum = 0, 0, 0
        for command, value in self.commands:
            if command == 'forward':
                forward_sum += int(value)
            elif command == 'down':
                down_sum += int(value)
            elif command == 'up':
                up_sum += int(value)
        return forward_sum, down_sum, up_sum

    def _second_calculation(self) -> int:
        target, forward_sum, depth = 0, 0, 0
        for command, value in self.commands:
            if command == 'forward':
                forward_sum += int(value)
                depth += int(value) * target
            elif command == 'down':
                target += int(value)
            elif command == 'up':
                target -= int(value)
        return forward_sum * depth



if __name__ == "__main__":
    start_time = perf_counter()
    print(Dive(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0.001 seconde
