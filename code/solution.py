import time
from typing import List

import numpy as np
from get_input import get_input

class Solution():
    def __init__(self, day: int, year: int =2024) -> None:
        self.inp = get_input(day, year)
        self.parse_input()
        
    def parse_input(self, type=None) -> None:
        if type == 'str_map':
            self.map = np.array([list(x) for x in self.inp])
        elif type == 'int_map':
            self.map = np.array([list(x) for x in self.inp], dtype=int)
        else:
            pass

    def problem_1(self) -> int:
        return 0

    def problem_2(self) -> int:
        return 0
    
    def __str__(self):
        str_1 = time.time()
        sol_1 = self.problem_1()
        end_1 = time.time()
        sol_2 = self.problem_2()
        end_2 = time.time()
        return f"Solution to problem 1: {sol_1} (took {end_1 - str_1:.5f}s)"\
               f"\nSolution to problem 2: {sol_2} (took {end_2 - end_1:.5f}s)"