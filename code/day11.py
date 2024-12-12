from collections import defaultdict

from solution import Solution

class Day11(Solution):
    def __init__(self):
        super().__init__(day=11, year=2024)

    def parse_input(self):
        self.inp = [int(x) for x in self.inp[0].split(' ')]
        # stones is a dictionary containing for each engraving 
        # the number of stones with that engaving.
        # in this way we only process each value once.
        self.stones = defaultdict(lambda: 0)
        for x in self.inp: self.stones[x] += 1

    def n_of_digits(self, x):
        count = 1
        while True:
            x = x // 10
            if x > 0: count += 1
            else: break
        return count    

    def deconcat(self, x, ndig=None):
        split_at = (self.n_of_digits(x) if ndig is None else ndig) // 2
        snd = x % (10**split_at)
        fst = (x - snd) // (10**split_at) 
        return fst, snd
    
    def blink(self, stones):
        new_stones = defaultdict(lambda: 0)
        # rules: 
        # 1) change 0 --> 1
        new_stones[1] = stones[0]
        for x in stones:
            if x == 0: continue # already done 0
            # 2) if even digits, split in two
            ndig = self.n_of_digits(x)
            if ndig % 2 == 0:
                fst, snd = self.deconcat(x, ndig)
                new_stones[fst] += stones[x]
                new_stones[snd] += stones[x]
            else: 
                # 3) multiply all rest by 2024
                new_stones[x * 2024] += stones[x]
        return new_stones

    def problem_1(self):
        stones = self.stones.copy()
        for _ in range(25):
            stones = self.blink(stones)
        return sum(list(stones.values()))
    
    def problem_2(self):
        stones = self.stones.copy()
        for _ in range(75):
            stones = self.blink(stones)
        return sum(list(stones.values()))

    
if __name__ == '__main__':
    print(Day11())