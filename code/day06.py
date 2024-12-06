from collections import defaultdict
import numpy as np
from tqdm import tqdm
from solution import Solution

class Day06(Solution):
    def __init__(self):
        super().__init__(day=6, year=2024)

    def move(self, pos, char, map):
        y, x = pos
        if char == '^':
            if y == 0: return None, None
            if map[y-1, x] != '#': return '^', (y-1, x)
            else: return '>', (y, x)
        if char == '>':
            if x == map.shape[0] - 1: return None, None
            if map[y, x+1] != '#': return '>', (y, x+1)
            else: return 'v', (y, x)
        if char == 'v':
            if y == map.shape[1] - 1: return None, None
            if map[y+1, x] != '#': return 'v', (y+1, x)
            else: return '<', (y, x)
        if char == '<':
            if x == 0: return None, None
            if map[y, x-1] != '#': return '<', (y, x-1)
            else: return '^', (y, x)

    def problem_1(self):
        visited_pos = set()
        cur_char = '^'
        init_pos = np.where(self.map == cur_char)
        y, x = init_pos[0][0], init_pos[1][0]
        visited_pos.add((y, x))
        while True:
            cur_char, new_pos = self.move((y, x), cur_char, map=self.map)
            if cur_char is None: break
            y, x = new_pos
            visited_pos.add(new_pos)
        return len(visited_pos)
    
    def problem_2(self):
        loop_count = 0
        init_pos = np.where(self.map == '^')
        y_start, x_start = init_pos[0][0], init_pos[1][0]
        for (y_obst, x_obst) in tqdm(np.ndindex(self.map.shape), 
                                     total=self.map.shape[0]*self.map.shape[1],
                                     desc='Placing obstacles for problem 2'):
            if (y_obst, x_obst) == (y_start, x_start): continue
            y, x = y_start, x_start
            cur_char = '^'
            map_copy = self.map.copy()
            map_copy[y_obst, x_obst] = '#'
            changes_to_up = set(); check_new_char = False
            while True:
                check_new_char = cur_char != '^'
                cur_char, new_pos = self.move((y, x), cur_char, map=map_copy)
                if cur_char is None: break
                # Check if char has changed to ^
                if check_new_char and cur_char == '^':
                    if new_pos in changes_to_up:
                        loop_count += 1; break
                    changes_to_up.add(new_pos)
                y, x = new_pos
        return loop_count
        
    def parse_input(self):
        self.map = np.array([list(x) for x in self.inp])
    
if __name__ == '__main__':
    print(Day06())