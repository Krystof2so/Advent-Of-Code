from itertools import product
from pathlib import Path
from time import perf_counter

PUZZLE = "puzzle.txt"


class InterpreterIntcode:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.datas: list[int] = self._extract_datas()
        self.all_pairs_noun_verb: list[tuple[int, int]] = [(noun, verb) for noun, verb in product(range(100), repeat=2)]
        self.ref_value: int = 19690720

    def __str__(self) -> str:
        return (f"Valeur après l'arrêt du programme : {self._change_intcode()}\n"
                f"Valeur de l'arrêt du programme pour {self.ref_value} : {self._to_19690720()}")

    def _extract_datas(self) -> list[int]:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            numbers_list = list(map(int, f.readline().strip().split(",")))
        numbers_list[1:3] = [12, 2]  # Affectation en une seule opération
        return numbers_list

    def _change_intcode(self) -> int:
        instruction_pointeur = 0
        while self.datas[instruction_pointeur] != 99:
            code1, code2, code3 = self.datas[instruction_pointeur + 1:instruction_pointeur + 4]
            self.datas[code3] = (self.datas[code1] + self.datas[code2] if self.datas[instruction_pointeur] == 1 else self.datas[code1] * self.datas[code2])
            instruction_pointeur += 4  # Avancer de 4 instructions
        return self.datas[0]

    def _to_19690720(self) -> int | None:
        for int_tuple in self.all_pairs_noun_verb:
            self.datas = self._extract_datas()
            self.datas[1:3] = [int_tuple[0], int_tuple[1]]
            if self._change_intcode() == self.ref_value:
                return 100 * int_tuple[0]  + int_tuple[1]
            

if __name__=="__main__":
    start_time = perf_counter()
    print(InterpreterIntcode(PUZZLE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.5f} seconde.")  # 0.4500 seconde


