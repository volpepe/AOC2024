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
    
    def sort(self, update):
        page_set = set(update)
        # Work on the subset of rules containing the relationships between items
        # in the update
        involved_rules = [rule for rule in self.rules 
                                if rule[0] in page_set
                                and rule[1] in page_set]
        # Sort the page set by checking item by item and how they interact with
        # other pages through the involved rules
        sorted_pages, sorted_page_set = [], set()
        for page in update:
            idx = 0
            # Collect the indices of items that are smaller in the order and have already been sorted.
            # Note that this can also be done by checking items that are greater in order.
            greater_than = [ rule[0] for rule in involved_rules if rule[1] == page ]
            more_than_idxs = [ sorted_pages.index(item) for item in greater_than if item in sorted_page_set ]
            # The page must be placed to the right of the element that is currently considered
            # the closest smaller
            if len(more_than_idxs) > 0:
                idx = max(more_than_idxs) + 1
            sorted_pages.insert(idx, page)
            sorted_page_set.add(page)
        return sorted_pages

    def problem_2(self):
        res = 0
        for update in self.updates:
            if not self.is_in_correct_order(update):
                update = self.sort(update)
                res += self.get_middle_page(update)
        return res


if __name__ == '__main__':
    print(Day05())