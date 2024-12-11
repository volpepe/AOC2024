from tqdm import tqdm
from solution import Solution

class Day10(Solution):
    def __init__(self):
        super().__init__(day=11, year=2024)

    def parse_input(self):
        self.stones = {i: int(x) for i, x in enumerate(self.inp[0].split(' '))}

    def n_of_digits(self, x):
        count = 1
        while True:
            x = x // 10
            if x > 0: count += 1
            else: break
        return count    

    def deconcat(self, x):
        split_at = self.n_of_digits(x) // 2
        snd = x % (10**split_at)
        fst = (x - snd) // (10**split_at) 
        return fst, snd
    
    def blink(self, stones: list):
        i = 0
        for i in range(len(stones)):
            # rules: 1) change 0 --> 1
            if stones[i] == 0: stones[i] = 1
            elif self.n_of_digits(stones[i]) % 2 == 0:
                fst, snd = self.deconcat(stones[i])
                stones[i] = fst
                stones[len(stones)] = snd # skip new stone
            else: stones[i] *= 2024
        return stones

    def problem_1(self):
        stones = self.stones.copy()
        for _ in tqdm(range(25)):
            stones = self.blink(stones)
        return len(stones)
    
    def problem_2(self):
        return 0
        # stones = self.stones.copy()
        # for _ in tqdm(range(40)):
        #     stones = self.blink(stones)
        # return len(stones)

    
if __name__ == '__main__':
    print(Day10())