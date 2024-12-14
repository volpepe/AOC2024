import numpy as np
from solution import Solution

class Day10(Solution):
    def __init__(self):
        super().__init__(day=10, year=2024)

    def parse_input(self):
        super().parse_input(type='int_map')

    def in_bounds(self, y, x):
        return 0 <= y < self.map.shape[0] and 0 <= x < self.map.shape[1]

    def find_next_from(self, y, x):
        cur_val = self.map[y, x]; find_val = cur_val + 1
        next_steps = []
        if cur_val == 9: return [], True    # is_peak
        for (y_f, x_f) in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]: # up, right down, left
            if self.in_bounds(y_f, x_f) and self.map[y_f, x_f] == find_val:
                next_steps.append((y_f, x_f))
        return next_steps, False

    def problem_1(self):
        return self.solution()[0]
    
    def problem_2(self):
        return self.solution()[1]

    def solution(self):
        tot_peaks, tot_trails = 0, 0
        trailheads_y, trailheads_x = np.where(self.map == 0)
        for (y, x) in zip(trailheads_y, trailheads_x):
            explore_queue = [(y, x)]; peaks = set(); trails = 0
            while True:
                y, x = explore_queue[0]; del explore_queue[0]
                next_steps, is_peak = self.find_next_from(y, x) # basically a bfs
                explore_queue.extend(next_steps)
                if is_peak: peaks.add((y, x)); trails += 1
                if len(explore_queue) == 0: break
            tot_peaks += len(peaks); tot_trails += trails
        return tot_peaks, tot_trails

    
if __name__ == '__main__':
    print(Day10())