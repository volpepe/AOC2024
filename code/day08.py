import numpy as np
from solution import Solution
from itertools import permutations

class Day08(Solution):
    def __init__(self):
        super().__init__(day=8, year=2024)

    def parse_input(self):
        super().parse_input(type='str_map') 

    def draw_from(self, p1, p2, map, w=2):
        (y1, x1), (y2, x2) = p1, p2
        dy = abs(y1-y2); dx = abs(x1-x2)
        dy *= (w-1); dx *= (w-1)
        if y1 < y2:
            if y1-dy >= 0:   # else out of bounds
                # p1 is upper point
                if x1 <= x2:
                    if x1-dx >= 0:   # else out of bounds
                        # p1 is left point
                        map[y1-dy, x1-dx] = '#' 
                else:
                    if x1+dx < self.map.shape[1]:  # else out of bounds
                        # p1 is right point
                        map[y1-dy, x1+dx] = '#' 
        else:
            if y1+dy < self.map.shape[0]:   # else out of bounds
                # p1 is lower point
                if x1 <= x2:
                    if x1-dx >= 0:  # else out of bounds
                        # p1 is left point
                        map[y1+dy, x1-dx] = '#' 
                else:
                    if x1+dx < self.map.shape[1]:   # else out of bounds
                        # p1 is right point
                        map[y1+dy, x1+dx] = '#'
    
    def problem_1(self):
        frequencies = np.unique(self.map[self.map != '.'])
        count_map = np.full_like(self.map, '.')
        for freq in frequencies:
            y, x = np.where(self.map == freq)
            for p1, p2 in permutations(zip(y, x), 2):
                self.draw_from(p1, p2, count_map, w=2)
        return np.sum(count_map == '#')
    
    def problem_2(self):
        frequencies = np.unique(self.map[self.map != '.'])
        count_map = np.full_like(self.map, '.')
        for freq in frequencies:
            y, x = np.where(self.map == freq)
            for p1, p2 in permutations(zip(y, x), 2):
                for i in range(max(self.map.shape)):    # Very inefficient, but it works
                    self.draw_from(p1, p2, count_map, w=i+1)
        return np.sum(np.logical_or(count_map == '#', self.map != '.'))
    
if __name__ == '__main__':
    print(Day08())