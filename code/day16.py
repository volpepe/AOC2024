from collections import defaultdict
import copy
import numpy as np

from solution import Solution


class Day16(Solution):
    def __init__(self):
        super().__init__(day=16, year=2024)

    def parse_input(self):
        super().parse_input('str_map') 
        self.map = self.map[1:-1, 1:-1] # Remove borders
        self.start_pos = tuple([x[0] for x in np.where(self.map == 'S')])
        self.end_pos = tuple([x[0] for x in np.where(self.map == 'E')])

    def manhattan_dist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def heuristic_cost(self, cur_pos):
        # the heuristic cost is basically the manhattan distance to the end,
        # but if we turn by 90 degrees we need to add 1000 instead of just 1.
        # we return the cost for all adjacent nodes to cur_pos
        cur_dir = cur_pos[2]
        cost_up_to_n = {
            (cur_pos[0] + 1, cur_pos[1], 'v'): 1 
                if cur_dir == 'v' else np.inf,
            (cur_pos[0] - 1, cur_pos[1], '^'): 1 
                if cur_dir == '^' else np.inf,
            (cur_pos[0], cur_pos[1] + 1, '>'): 1 
                if cur_dir == '>' else np.inf,
            (cur_pos[0], cur_pos[1] - 1, '<'): 1 
                if cur_dir == '<' else np.inf,
            (cur_pos[0], cur_pos[1], 'v'): 1000
                if cur_dir == '<' or cur_dir == '>' else np.inf,
            (cur_pos[0], cur_pos[1], '^'): 1000
                if cur_dir == '<' or cur_dir == '>' else np.inf,
            (cur_pos[0], cur_pos[1], '>'): 1000
                if cur_dir == '^' or cur_dir == 'v' else np.inf,
            (cur_pos[0], cur_pos[1], '<'): 1000
                if cur_dir == '^' or cur_dir == 'v' else np.inf,
        }
        # remove impossible movements
        for n in cost_up_to_n:
            if  (n[0] != cur_pos[0] or n[1] != cur_pos[1]) and \
                (n[0] < 0 or n[0] >= self.map.shape[1] \
              or n[1] < 0 or n[1] >= self.map.shape[0] \
              or self.map[n[0], n[1]] == '#'):
                cost_up_to_n[n] = np.inf
        # reduces computations on illegal neighbours
        cost_up_to_n = {
            n: cost_up_to_n[n]
            for n in cost_up_to_n
            if not np.isinf(cost_up_to_n[n])
        }
        # cost from n to end. note that end is at the top right of the map
        # so in certain cases we will need to turn!
        cost_from_n_to_e = {
            pos: self.manhattan_dist((pos[0], pos[1]), self.end_pos) 
            for pos in cost_up_to_n
        }
        for choice in cost_from_n_to_e:
            dir_ = choice[2]
            if dir_ == '<' or dir_ == 'v': 
                cost_from_n_to_e[choice] += 1000
            elif dir_ == '^' and cur_pos[1] != self.map.shape[1] - 1: 
                cost_from_n_to_e[choice] += 1000
            elif dir_ == '>' and cur_pos[0] != 0:
                cost_from_n_to_e[choice] += 1000        
        return cost_up_to_n, cost_from_n_to_e        
    
    def find_best_path(self, map):
        # basically a*
        open_nodes_set = set([(self.start_pos[0], self.start_pos[1], '>')])
        # came_from maps each node to the node that immediately precedes it
        # in the cheapest path towards the end
        came_from = {(y, x, dir): None
                     for dir in ['<', '>', '^', 'v']
                     for y in range(map.shape[0])
                     for x in range(map.shape[1])}
        # this is the cost of the cheapest path from start to the node
        cost = {(y, x, dir): np.inf
                for dir in ['<', '>', '^', 'v']
                for y in range(map.shape[0])
                for x in range(map.shape[1])}
        cost[(self.start_pos[0], self.start_pos[1], '>')] = 0
        # this is the current estimate of the cost to reach the endpoint
        # if the path passes from the node
        fscore = {(y, x, dir): np.inf
                  for dir in ['<', '>', '^', 'v']
                  for y in range(map.shape[0])
                  for x in range(map.shape[1])}
         # At least one rotation + forward movements
        fscore[(self.start_pos[0], self.start_pos[1], '>')] = \
            self.manhattan_dist(self.start_pos, self.end_pos) + 1000

        def reconstruct_path(came_from, current):
            total_path = [current]
            while current in came_from:
                current = came_from[current]
                total_path.append(current)
            return total_path[::-1][1:]

        # Run until there are nodes to explore
        while True:
            if len(open_nodes_set) == 0:
                break

            # get the node in the open set with the lowest fscore
            current = min(open_nodes_set, key=lambda x: fscore[x])
            if current[:2] == self.end_pos:
                # found shortest path!
                return reconstruct_path(came_from, current)
            
            open_nodes_set.remove(current)

            # compute the costs of surrounding elements
            costs_up_to_neighbours, costs_from_neighbours_to_end = \
                self.heuristic_cost(current)

            for neighbour in costs_up_to_neighbours:
                tentative_cost = cost[current] + costs_up_to_neighbours[neighbour]
                if tentative_cost < cost[neighbour]:
                    # this path to the neighbour is better than any previous one
                    came_from[neighbour] = current
                    cost[neighbour] = tentative_cost
                    fscore[neighbour] = tentative_cost + costs_from_neighbours_to_end[neighbour]
                    if neighbour not in open_nodes_set:
                        open_nodes_set.add(neighbour)
        
        return None

    def score(self, best_path):
        cost = 0
        for i in range(1, len(best_path)):
            if best_path[i][2] != best_path[i - 1][2]:
                cost += 1000    # turn
            else:
                cost += 1   # straight
        return cost


    def problem_1(self):
        map = copy.deepcopy(self.map)
        best_path = self.find_best_path(map)
        return self.score(best_path)
    
    def problem_2(self):
        res = 0
        return res

    
if __name__ == '__main__':
    print(Day16())

