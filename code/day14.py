import copy
import re
import time

import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import cdist
from solution import Solution
from tqdm import tqdm

MAP_SIZE = (101, 103)


class Day14(Solution):
    def __init__(self):
        super().__init__(day=14, year=2024)

    def move_robots(self, robots):
        for r in robots:
            r[0] = (r[0] + r[2]) % MAP_SIZE[0]
            r[1] = (r[1] + r[3]) % MAP_SIZE[1]
        return robots
    
    def compute_safety_factor(self, robots):
        xh = MAP_SIZE[0] // 2
        yh = MAP_SIZE[1] // 2
        quadrants = { i: 0 for i in range(4) }
        safety_factor = 1
        for r in robots:
            if r[0] < xh:
                if r[1] < yh: quadrants[0] += 1
                elif r[1] > yh: quadrants[1] += 1
            elif r[0] > xh:
                if r[1] < yh: quadrants[2] += 1
                elif r[1] > yh: quadrants[3] += 1
        for q in quadrants:
            safety_factor *= quadrants[q]
        return safety_factor


    def parse_input(self):
        self.robots = [
            re.findall(
                r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)',
                self.inp[i]
            )[0]
            for i in range(len(self.inp))
        ]
        self.robots = [
            [int(r[0]), int(r[1]), int(r[2]), int(r[3])]
            for r in self.robots
        ]

    def problem_1(self):
        robots = copy.deepcopy(self.robots)
        for _ in range(100):
            robots = self.move_robots(robots)
        return self.compute_safety_factor(robots)
    
    def compute_closeness_score(self, robots):
        dists = cdist(
            np.array([[r[0], r[1]] for r in robots]),
            np.array([[r[0], r[1]] for r in robots]),
            'euclidean'
        )
        # count the number of distances that are pretty low
        return np.sum(dists < 10)
    
    def problem_2(self):
        robots = copy.deepcopy(self.robots)
        frame_with_max_score = 1; max_score = 0
        for i in tqdm(range(1, 10000), 
                      desc='Running simulation for problem 2'):
            robots = self.move_robots(robots)
            # when the avg distance from each robot from all
            # others is minimum, the robots are close and 
            # probably forming the tree
            score = self.compute_closeness_score(robots)
            if score > max_score:
                frame_with_max_score = i
                max_score = score
        return frame_with_max_score
    
if __name__ == '__main__':
    # visualization
    d = Day14()
    s = time.time()
    print(f"Solution to problem 1: {d.problem_1()} (took {time.time()-s:.5f}s)")
    s = time.time()
    prob_2_sol = d.problem_2()
    print(f"Solution to problem 2: {prob_2_sol} (took {time.time()-s:.5f}s)")
    robots = copy.deepcopy(d.robots)
    for _ in range(prob_2_sol): robots = d.move_robots(robots)
    plt.scatter(
        [r[0] for r in robots],
        [r[1] for r in robots],
        s=1, c='b'
    )
    plt.show()  # press 'q' to close the plot
