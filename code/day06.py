import numpy as np
from solution import Solution

class Day06(Solution):
    def __init__(self):
        super().__init__(day=6, year=2024)

    def move(self, pos, char):
        y, x = pos
        if char == '^':
            if y == 0: return None, None
            if self.map[y-1, x] != '#': return '^', (y-1, x)
            else: return '>', (y, x)
        if char == '>':
            if x == self.map.shape[0] - 1: return None, None
            if self.map[y, x+1] != '#': return '>', (y, x+1)
            else: return 'v', (y, x)
        if char == 'v':
            if y == self.map.shape[1] - 1: return None, None
            if self.map[y+1, x] != '#': return 'v', (y+1, x)
            else: return '<', (y, x)
        if char == '<':
            if x == 0: return None, None
            if self.map[y, x-1] != '#': return '<', (y, x-1)
            else: return '^', (y, x)

    def problem_1(self):
        visited_pos = set()
        cur_char = '^'
        init_pos = np.where(self.map == cur_char)
        y, x = init_pos[0][0], init_pos[1][0]
        visited_pos.add((y, x))
        while True:
            cur_char, new_pos = self.move((y, x), cur_char)
            if cur_char is None: break
            y, x = new_pos
            visited_pos.add(new_pos)
        return len(visited_pos)
    
    def problem_2(self):
        return super().problem_2()
    
    def parse_input(self):
        self.map = np.array([list(x) for x in self.inp])
    
if __name__ == '__main__':
    print(Day06())