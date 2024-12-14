from solution import Solution
import numpy as np


class Day04(Solution):
    def __init__(self):
        super().__init__(day=4, year=2024)

    def parse_input(self):
        super().parse_input(type='str_map')

    def lookforstraround(self, r, c, findm='MAS'):
        words = []
        resp_up_bound = r >= 3
        resp_low_bound = r <= self.map.shape[0] - 4
        resp_left_bound = c >= 3
        resp_right_bound = c <= self.map.shape[1] - 4
        # UP
        if resp_up_bound:
            words.append(''.join(self.map[r-3:r, c])[::-1])
            # UP RIGHT
            if resp_right_bound:
                words.append(''.join(np.diag(np.rot90(self.map[r-3:r, c+1:c+4], k=3))))
        # RIGHT
        if resp_right_bound:
            words.append(''.join(self.map[r, c+1:c+4]))
            # DOWN RIGHT
            if resp_low_bound:
                words.append(''.join(np.diag(self.map[r+1:r+4, c+1:c+4])))
        # DOWN
        if resp_low_bound:
            words.append(''.join(self.map[r+1:r+4, c]))
            # DOWN LEFT
            if resp_left_bound:
                words.append(''.join(np.diag(np.rot90(self.map[r+1:r+4, c-3:c], k=3)))[::-1])
        # LEFT
        if resp_left_bound:
            words.append(''.join(self.map[r, c-3:c])[::-1])
            # UP LEFT
            if resp_up_bound:
                words.append(''.join(np.diag(self.map[r-3:r, c-3:c]))[::-1])
        return sum([x == findm for x in words])

    def lookforx_mas(self, r, c):
        count = 0
        if 1 <= r <= self.map.shape[0] - 2 and 1 <= c <= self.map.shape[1] - 2:
            if self.map[r-1, c-1] == 'M' and self.map[r+1, c+1] == 'S': count += 1
            if self.map[r+1, c+1] == 'M' and self.map[r-1, c-1] == 'S': count += 1
            if self.map[r-1, c+1] == 'M' and self.map[r+1, c-1] == 'S': count += 1
            if self.map[r+1, c-1] == 'M' and self.map[r-1, c+1] == 'S': count += 1
        return count == 2

    def problem_1(self):
        res = 0
        rows, cols = np.where(self.map == 'X')
        for r, c in zip(rows, cols):
            res += self.lookforstraround(r, c)
        return res

    def problem_2(self):
        res = 0
        rows, cols = np.where(self.map == 'A')
        for r, c in zip(rows, cols):
            res += self.lookforx_mas(r, c)
        return res
    

if __name__ == "__main__":
    print(Day04())