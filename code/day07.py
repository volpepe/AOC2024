from solution import Solution
from itertools import product

class Day07(Solution):
    def __init__(self):
        super().__init__(day=7, year=2024)

    def parse_input(self):
        self.results = [int(x.split(':')[0]) for x in self.inp]
        self.operands = [[int(a) for a in x.split(' ')[1:]] for x in self.inp]

    def n_of_digits(self, x):
        count = 1
        while True:
            x = x // 10
            if x > 0: count += 1
            else: break
        return count        

    def is_possible(self, i, allowed_ops=['+','*']):
        ops = self.operands[i]
        res = self.results[i]
        allowed_ops_lambdas = []
        for op in allowed_ops:
            if op == '+': allowed_ops_lambdas.append(lambda a,b: a+b)
            if op == '*': allowed_ops_lambdas.append(lambda a,b: a*b)
            if op == '||': allowed_ops_lambdas.append(lambda a,b: a*10**self.n_of_digits(b)+b)
        for operations in product(allowed_ops_lambdas, repeat=len(ops)-1):
            tot = ops[0]
            for opidx in range(len(ops)-1):
                tot = operations[opidx](tot, ops[opidx+1])
            if tot == res: return True
        return False
    
    def solution(self, allowed_ops=['+','*']):
        res = 0
        for i in range(len(self.results)):
            if self.is_possible(i, allowed_ops):
                res += self.results[i]
        return res
    
    def problem_1(self):
        return self.solution()
    
    def problem_2(self):
        return self.solution(allowed_ops=['+','*','||'])
    
if __name__ == '__main__':
    print(Day07())