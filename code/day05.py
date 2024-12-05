import copy
from functools import cmp_to_key
from solution import Solution

class Day05(Solution):
    def __init__(self):
        super().__init__(day=5, year=2024)

    def parse_input(self):
        self.rules = [x for x in self.inp if '|' in x]
        self.updates = [x for x in self.inp if ',' in x]
        self.rules = [tuple([int(a) for a in x.split('|')]) 
                      for x in self.rules]
        self.updates = [[int(a) for a in x.split(',')]
                        for x in self.updates]
        return super().parse_input()
    
    def get_middle_page(self, update):
        return update[len(update) // 2]
    
    def is_in_correct_order(self, update):
        page_set = set(update)
        for idx, page in enumerate(update):
            # Check every rule involving the page. Only check precedence rules.
            involved_rules = [rule for rule in self.rules 
                              if rule[0] == page]
            for rule in involved_rules:
                # If the other page is not present in the update, go to next page
                if rule[1] not in page_set: continue
                # Otherwise, check that the other page is later in the update
                elif update.index(rule[1]) < idx: return False
        # If never returned False, return True
        return True

    def problem_1(self):
        res = 0
        for update in self.updates:
            if self.is_in_correct_order(update):
                res += self.get_middle_page(update)
        return res
    

    def problem_2(self):
        res = 0
        # for update in self.updates:
        #     if not self.is_in_correct_order(update):
        #         update = self.sort(update)
        #         res += self.get_middle_page(update)
        #         break
        return res


if __name__ == '__main__':
    print(Day05())