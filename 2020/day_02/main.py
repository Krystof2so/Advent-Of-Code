from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


class PasswordPolicy:

    def __init__(self, puzzle: str) -> None:
        self.puzzle: str = puzzle
        self.all_datas: tuple[tuple[int, int, str, str]] = self._extract_datas()

    def __str__(self):
        return (f"Nombre de mots de passe valides (selon l'ancienne politique): {self._valid_passwords(1)}\n"
                f"Nombre de mots de passe valides (nouvelle politique): {self._valid_passwords(2)}")

    def _extract_datas(self) -> tuple:
        with (Path(__file__).parent / self.puzzle).open("r", encoding="utf-8") as f:
            return tuple(
                (int(lim_min), int(lim_max), letter, password_str)
                for line in f
                for policy, password_str in [line.strip().split(": ")]
                for limits, letter in [policy.split(" ")]
                for lim_min, lim_max in [limits.split("-")]
            )

    def _new_passwd(self, passwd: tuple[int, int, str, str]) -> bool:
        min_lim, max_lim, char, password = passwd
        return (password[min_lim - 1] == char) != (password[max_lim - 1] == char)

    def _old_passwd(self, passwd: tuple[int, int, str, str]) -> bool:
        min_lim, max_min, char, password = passwd
        return min_lim <= password.count(char) <= max_min 

    def _valid_passwords(self, part: int = 1) -> int:
        return sum(self._old_passwd(passwd) if part == 1 else self._new_passwd(passwd) for passwd in self.all_datas)


if __name__ == "__main__":
    start_time = perf_counter()
    print(PasswordPolicy(DATAS_FILE))
    print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # 0.001 seconde
