from collections import defaultdict
from solution import Solution

class Day01(Solution):
    def __init__(self):
        super().__init__(day=1, year=2024)

    def parse_input(self):
        self.l1 = []
        self.l2 = []
        for line in self.inp:
            a1, a2 = line.split('   ')
            self.l1.append(int(a1))
            self.l2.append(int(a2))

    def problem_1(self) -> int:
        l1_sorted, l2_sorted = sorted(self.l1), sorted(self.l2)
        tot_diff = 0
        for i in range(len(l1_sorted)):
            tot_diff += abs(l1_sorted[i] - l2_sorted[i])
        return tot_diff
    
    def problem_2(self) -> int:
        binc = defaultdict(lambda: 0)
        score = 0
        for el in self.l2: binc[el] += 1
        for el in self.l1: score += (el * binc[el])
        return score

if __name__ == '__main__':
    print(Day01())