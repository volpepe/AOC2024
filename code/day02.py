from solution import Solution


class Day02(Solution):
    def __init__(self):
        super().__init__(day=2, year=2024)

    def parse_input(self):
        self.reports = [[int(item) for item in x.split(' ')] for x in self.inp]

    def is_damp_safe(self, report):
        return any([self.is_safe(report[:i] + report[i+1:]) 
                    for i in range(len(report))])

    def is_safe(self, report):
        incr = report[1] > report[0]
        for i in range(1, len(report)):
            if (incr and report[i] <= report[i-1]) or \
               (not incr and report[i] >= report[i-1]):
                return 0
            if (incr and report[i-1] + 3 < report[i]) or \
               (not incr and report[i-1] - 3 > report[i]):
                return 0
        return 1

    def problem_1(self):
        safe_count = 0
        for rep in self.reports: safe_count += self.is_safe(rep)
        return safe_count
    
    def problem_2(self):
        safe_count = 0
        for rep in self.reports: safe_count += self.is_damp_safe(rep)
        return safe_count
    

if __name__ == '__main__':
    print(Day02())