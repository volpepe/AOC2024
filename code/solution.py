from typing import List
from get_input import get_input

class Solution():
    def __init__(self, day: int, year: int =2024) -> None:
        self.inp = get_input(day, year)
        self.parse_input()
        
    def parse_input(self) -> None:
        pass

    def problem_1(self) -> int:
        raise NotImplementedError

    def problem_2(self) -> int:
        raise NotImplementedError
    
    def __str__(self):
        sol_1 = self.problem_1()
        sol_2 = self.problem_2()
        return f"Solution to problem 1: {sol_1}\nSolution to problem 2: {sol_2}"