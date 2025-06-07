import functools
from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"

def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")
        return result
    return _timer

class CrossedWires:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.wire1_path, self.wire2_path = self._extract_datas()
        self.wire1_points, self.wire2_points = self._trace_wire_paths()

    @timer
    def display_result(self) -> None:
        closest_intersection = self._find_closest_intersection()
        fewest_combined_steps = self._find_fewest_combined_steps()
        print(f"Distance de Manhattan de l'intersection la plus proche : {closest_intersection}")
        print(f"Nombre total d'étapes minimales pour atteindre une intersection : {fewest_combined_steps}")

    def _extract_datas(self) -> tuple[list[str], list[str]]:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            wire1_path = f.readline().strip().split(',')
            wire2_path = f.readline().strip().split(',')
        return wire1_path, wire2_path

    def _trace_wire_paths(self) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]]:
        def trace_path(path):
            x, y = 0, 0
            steps = 0
            points = {}
            for move in path:
                direction = move[0]
                distance = int(move[1:])
                for _ in range(distance):
                    if direction == 'R':
                        x += 1
                    elif direction == 'L':
                        x -= 1
                    elif direction == 'U':
                        y += 1
                    elif direction == 'D':
                        y -= 1
                    steps += 1
                    points[(x, y)] = steps
            return points

        wire1_points = trace_path(self.wire1_path)
        wire2_points = trace_path(self.wire2_path)
        return wire1_points, wire2_points

    def _find_closest_intersection(self) -> int:
        intersections = set(self.wire1_points.keys()) & set(self.wire2_points.keys())
        closest_intersection = min(abs(x) + abs(y) for x, y in intersections)
        return closest_intersection

    def _find_fewest_combined_steps(self) -> int:
        intersections = set(self.wire1_points.keys()) & set(self.wire2_points.keys())
        fewest_combined_steps = min(self.wire1_points[coord] + self.wire2_points[coord] for coord in intersections)
        return fewest_combined_steps


if __name__ == "__main__":
    CrossedWires(DATAS_FILE).display_result()

