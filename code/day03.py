from solution import Solution
import re

class Day03(Solution):
    def __init__(self):
        super().__init__(day=3, year=2024)

    def parse_input(self):
        self.inp = "".join(self.inp)
    
    def count_in_span(self, span):
        res = 0
        for mult in re.findall(r'mul\((\d+),(\d+)\)', span):
            res += int(mult[0]) * int(mult[1])
        return res
    
    def find_spans(self):
        activate_idxs = [0] + [m.span()[1] for m in re.finditer(r"do\(\)", self.inp)]
        a_s = set(activate_idxs)
        deactivate_idxs = [m.span()[0] for m in re.finditer(r'don\'t\(\)', self.inp)]
        d_s = set(deactivate_idxs)
        all_idxs = sorted(activate_idxs + deactivate_idxs)
        splits = []; active = False
        for idx in all_idxs:
            if idx in a_s and not active:
                splits.append(idx)
                active = True
            if idx in d_s and active:
                splits[-1] = (splits[-1], idx)
                active = False
        return splits

    def problem_1(self):
        return self.count_in_span(self.inp)
    
    def problem_2(self):
        res = 0
        splits = self.find_spans()
        for split in splits:
            res += self.count_in_span(self.inp[split[0]:split[1]])
        return res
    
if __name__ == '__main__':
    print(Day03())