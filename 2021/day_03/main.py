import functools
from pathlib import Path
from time import perf_counter

DATAS_FILE = "puzzle.txt"


def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Temps d'exécution : {perf_counter() - start_time:.6f} seconde")  # seconde
        return result
    return _timer


class BinaryDiagnostic:

    def __init__(self) -> None:
        self.all_datas: list[str] = self._extract_datas() 

    @timer
    def display_result(self) -> None:
        gamma, epsilon = self._gamma_epsilon_rate()
        oxygen = self._oxygen_generator_rating()
        co2 = self._co2_scrubber_rating()
        print(f"Le produit de Gamma et Epsilon : {gamma * epsilon}")
        print(f"Le taux de support vie : {oxygen * co2}")

    def _extract_datas(self) -> list:
        with (Path(__file__).parent / DATAS_FILE).open("r", encoding="utf-8") as f:
            list_datas = [line.strip() for line in f]
        return list_datas

    def _gamma_epsilon_rate(self) -> tuple[int, int]:
        gamma_binary, epsilon_binary = [], []
        for i in range(len(self.all_datas[0])):
            number_0 = sum([1 for data in self.all_datas if data[i] == "0"])
            number_1 = sum([1 for data in self.all_datas if data[i] == "1"])
            gamma_binary.append("1" if number_1 > number_0 else "0")
            epsilon_binary.append("0" if number_1 > number_0 else "1")
        gamma_binary_str = "".join(gamma_binary)
        epsilon_binary_str = "".join(epsilon_binary)
        return int(gamma_binary_str, 2), int(epsilon_binary_str, 2)

    def _oxygen_generator_rating(self) -> int:
        candidates = self.all_datas.copy()
        bit_position = 0
        while len(candidates) > 1:
            number_0 = sum([1 for data in candidates if data[bit_position] == "0"])
            number_1 = sum([1 for data in candidates if data[bit_position] == "1"])
            most_common_bit = "1" if number_1 >= number_0 else "0"
            candidates = [data for data in candidates if data[bit_position] == most_common_bit]
            bit_position += 1
        return int(candidates[0], 2)

    def _co2_scrubber_rating(self) -> int:
        candidates = self.all_datas.copy()
        bit_position = 0
        while len(candidates) > 1:
            number_0 = sum([1 for data in candidates if data[bit_position] == "0"])
            number_1 = sum([1 for data in candidates if data[bit_position] == "1"])
            least_common_bit = "0" if number_0 <= number_1 else "1"
            candidates = [data for data in candidates if data[bit_position] == least_common_bit]
            bit_position += 1
        return int(candidates[0], 2)


if __name__ == "__main__":
    BinaryDiagnostic().display_result()
