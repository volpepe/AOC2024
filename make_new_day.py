import os
import argparse

def parse_args():
    argps = argparse.ArgumentParser()
    argps.add_argument('-d', '--day', type=int, help="Day")
    argps.add_argument('-y', '--year', type=int, default=2024, help="Year")
    return argps.parse_args()

if __name__ == '__main__':
    args = parse_args()
    with open(os.path.join('code', f'day{args.day:02d}.py'), 'w') as f:
        f.write(
'''\
from collections import defaultdict
import numpy as np

from solution import Solution


class Day{}(Solution):
    def __init__(self):
        super().__init__(day={}, year={})

    def parse_input(self):
        return super().parse_input() 

    def problem_1(self):
        res = 0
        return res
    
    def problem_2(self):
        res = 0
        return res

    
if __name__ == '__main__':
    print(Day{}())

'''.format(
    args.day, args.day, args.year, args.day
)
        )