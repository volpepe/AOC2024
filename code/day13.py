import numpy as np
from scipy.optimize import milp, LinearConstraint
import re

from solution import Solution


class Day13(Solution):
    def __init__(self):
        super().__init__(day=13, year=2024)

    def parse_input(self):
        self.inp = '\n'.join(self.inp)
        self.problems = \
            re.findall(
            r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y=(\d+)',
            self.inp)
        self.problems = [
            (int(p[0]), int(p[1]), int(p[2]), int(p[3]), int(p[4]), int(p[5]))
            for p in self.problems
        ]

    def get_cost(self, push_a, push_b):
        return push_a * 3 + push_b

    def solve(self, prob, max_pushes=None, sol_adder=0):
        # yeah i'm using a milp solver fuck off
        mult_a_x, mult_a_y, mult_b_x, mult_b_y, sol_x, sol_y = prob
        sol_x, sol_y = sol_x + sol_adder, sol_y + sol_adder
        A = np.array([
            # we need =, which is a combo of <= and >=, so of <= and (-) <= (-)
            [mult_a_x, mult_b_x],
            [-mult_a_x, -mult_b_x],
            [mult_a_y, mult_b_y],
            [-mult_a_y, -mult_b_y]
        ])
        b_u = np.array([sol_x, -sol_x, sol_y, -sol_y])
        b_l = np.full_like(b_u, -np.inf, dtype=float)
        c = np.array([3, 1])   # cost = 3*push_a + 1*push_b
        constraints = LinearConstraint(A=A, lb=b_l, ub=b_u)
        integrality = np.ones_like(c)
        res = milp(c=c, constraints=constraints, integrality=integrality)
        if not res.success: 
            # failed to solve
            return False, 0
        # solved but might be out of bounds
        p_a, p_b = [int(x) for x in res.x]
        if max_pushes is not None and (p_a > max_pushes or p_b > max_pushes):
            return False, 0
        return res.success, self.get_cost(p_a, p_b)

    def problem_1(self):
        cost = 0
        for prob in self.problems:
            solved, p_cost = self.solve(prob, max_pushes=100)
            if solved: cost += p_cost
        return cost
    
    def problem_2(self):
        cost = 0
        for prob in self.problems:
            solved, p_cost = self.solve(prob, sol_adder=10000000000000)
            if solved: cost += p_cost
        return cost

    
if __name__ == '__main__':
    print(Day13())

