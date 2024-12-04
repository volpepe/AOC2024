from solution import Solution
import numpy as np


class Day04(Solution):
    def __init__(self):
        super().__init__(day=4, year=2024)

    def parse_input(self):
        self.inp = np.array([list(x) for x in self.inp])

    def lookforstraround(self, r, c, findm='MAS'):
        words = []
        resp_up_bound = r >= 3
        resp_low_bound = r <= self.inp.shape[0] - 4
        resp_left_bound = c >= 3
        resp_right_bound = c <= self.inp.shape[1] - 4
        # UP
        if resp_up_bound:
            words.append(''.join(self.inp[r-3:r, c])[::-1])
            # UP RIGHT
            if resp_right_bound:
                words.append(''.join(np.diag(np.rot90(self.inp[r-3:r, c+1:c+4], k=3))))
        # RIGHT
        if resp_right_bound:
            words.append(''.join(self.inp[r, c+1:c+4]))
            # DOWN RIGHT
            if resp_low_bound:
                words.append(''.join(np.diag(self.inp[r+1:r+4, c+1:c+4])))
        # DOWN
        if resp_low_bound:
            words.append(''.join(self.inp[r+1:r+4, c]))
            # DOWN LEFT
            if resp_left_bound:
                words.append(''.join(np.diag(np.rot90(self.inp[r+1:r+4, c-3:c], k=3)))[::-1])
        # LEFT
        if resp_left_bound:
            words.append(''.join(self.inp[r, c-3:c])[::-1])
            # UP LEFT
            if resp_up_bound:
                words.append(''.join(np.diag(self.inp[r-3:r, c-3:c]))[::-1])
        return sum([x == findm for x in words])

    def lookforx_mas(self, r, c):
        count = 0
        if 1 <= r <= self.inp.shape[0] - 2 and 1 <= c <= self.inp.shape[1] - 2:
            if self.inp[r-1, c-1] == 'M' and self.inp[r+1, c+1] == 'S': count += 1
            if self.inp[r+1, c+1] == 'M' and self.inp[r-1, c-1] == 'S': count += 1
            if self.inp[r-1, c+1] == 'M' and self.inp[r+1, c-1] == 'S': count += 1
            if self.inp[r+1, c-1] == 'M' and self.inp[r-1, c+1] == 'S': count += 1
        return count == 2

    def problem_1(self):
        res = 0
        rows, cols = np.where(self.inp == 'X')
        for r, c in zip(rows, cols):
            res += self.lookforstraround(r, c)
        return res

    def problem_2(self):
        res = 0
        rows, cols = np.where(self.inp == 'A')
        for r, c in zip(rows, cols):
            res += self.lookforx_mas(r, c)
        return res
    

if __name__ == "__main__":
    print(Day04())