from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class RockPaperScissors:

    WIN = {"A": "Y", "B": "Z", "C": "X"}
    NUL = {"A": "X", "B": "Y", "C": "Z"}
    VALUES = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    SCORES = {"X": 0, "Y": 3, "Z": 6}

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.all_rounds = self._extract_datas()

    def __str__(self):
        first_score, second_score = self._score_part()
        return f"Premier score = {first_score}\nSecond score = {second_score}"

    @staticmethod
    def _identify_object(round: str) -> int:
        opponent, outcome = round
        if outcome == "Y":
            return RockPaperScissors.VALUES[opponent]
        elif outcome == "X":
            return RockPaperScissors.VALUES[{"A": "C", "B": "A", "C": "B"}[opponent]]
        return RockPaperScissors.VALUES[{"A": "B", "B": "C", "C": "A"}[opponent]]

    @staticmethod
    def _calculate_score(round: str, part: int) -> int:
        opponent, outcome = round
        if part == 1:
            shape_score = RockPaperScissors.VALUES[outcome]
            if RockPaperScissors.WIN[opponent] == outcome:
                return shape_score + 6
            elif RockPaperScissors.NUL[opponent] == outcome:
                return shape_score + 3
            return shape_score
        return RockPaperScissors._identify_object(round) + RockPaperScissors.SCORES[outcome]

    def _extract_datas(self) -> list:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            return [line.strip().replace(" ", "") for line in f]

    def _score_part(self) -> tuple[int, int]:
        return (
            sum(self._calculate_score(round, 1) for round in self.all_rounds),
            sum(self._calculate_score(round, 2) for round in self.all_rounds)
            )


if __name__ == "__main__":
    start_time = perf_counter()
    print(RockPaperScissors(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0.0028 seconde
