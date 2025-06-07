from pathlib import Path
from time import perf_counter


DIGITAL_KEYBOARD = {  # (x, y): touche clavier - 1ERE PARTIE
                    (1, 1): '1', (2, 1): '2', (3, 1): '3',  # 1ere ligne (1, 2, 3): y = 1
                    (1, 2): '4', (2, 2): '5', (3, 2): '6',  # 2e ligne (4, 5, 6): y = 2
                    (1, 3): '7', (2, 3): '8', (3, 3): '9'   # 3e ligne (7, 8, 9): y = 3
                    }

DIGITAL_KEYBOARD_2 = {  # (x, y): touche clavier - 2E PARTIE
                      (2,1): '1',                                                  # 1ere lig: y = 1
                      (1,2): '2', (2,2): '3', (3,2): '4',                          # 2e lig: y = 2
                      (0,3): '5', (1,3): '6', (2,3): '7', (3,3): '8', (4,3): '9',  # 3e lig: y = 3  
                      (1,4): 'A', (2,4): 'B', (3,4): 'C',                          # 4e lig: y = 4
                      (2,5): 'D'                                                   # 5e lig: y = 5
                      }

MOVES = {  # Mouvement: tuple incrémentation/décrémentation de x ou y
         "U": (0, -1), "D": (0, 1),  # Changement de ligne
         "L": (-1, 0), "R": (1, 0)   # Changement de colonne
         }

PUZZLE = "puzzle.txt"


class BathroomSecurity:
    
    def __init__(self, puzzle: str, challenge: int=1):
        self.puzzle: str = puzzle
        self.challenge: int = challenge
        self.digital_keyboard: dict = DIGITAL_KEYBOARD if self.challenge == 1 else DIGITAL_KEYBOARD_2
        self.all_codes: list[str] = self._all_codes()
        self.x, self.y = (2, 2) if self.challenge == 1 else (1, 3)  # Position initiale de la touche 5

    def __str__(self):
        return f"Code secret {'1' if self.challenge == 1 else '2'} = {self._secret_code()}"

    def _all_codes(self) -> list[str]:
        """Retourne l'extracation du puzzle : chaque ligne étant alors une chaîne de caractères insérée dans une liste"""
        full_path = Path(__file__).parent / self.puzzle
        with open(full_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def _digicode_number(self, code) -> str:
        """Retourne un des chiffres du digicode."""
        for d in code:
            self.x, self.y = self._new_coordinates(*MOVES[d]) 
        return self.digital_keyboard[(self.x, self.y)]

    def _new_coordinates(self, new_x: int, new_y: int) -> tuple[int, int]:
        """Retoune des coordonées dans la limite de la taille du digicode."""
        new_x, new_y = self.x + new_x, self.y + new_y
        if (new_x, new_y) in self.digital_keyboard:
            return new_x, new_y
        return self.x, self.y

    def _secret_code(self) -> str:
        """Constuit et retourne le code secret"""
        return "".join(map(self._digicode_number, self.all_codes))
    

if __name__ == "__main__":
    start_time = perf_counter()
    print(BathroomSecurity(PUZZLE))
    print(BathroomSecurity(PUZZLE, challenge=2))
    print(f"Temps d'exécution : {perf_counter() - start_time:.5f} seconde(s)")  # 0.002
