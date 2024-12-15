import copy
import numpy as np
import re

from solution import Solution


class Day15(Solution):
    def __init__(self):
        super().__init__(day=15, year=2024)
        self.command_impl = {
            '^': lambda x: [x[0]-1, x[1]],
            'v': lambda x: [x[0]+1, x[1]],
            '<': lambda x: [x[0], x[1]-1],
            '>': lambda x: [x[0], x[1]+1]
        }

    def parse_input(self):
        mp = []; commands = ''; i = 0
        while True:
            if self.inp[i] == '': break
            mp.append(self.inp[i]); i += 1
        commands = ''.join(self.inp[i+1:])
        self.commands = re.findall(r'(\^|v|<|>)', commands) 
        self.inp = mp
        super().parse_input(type='str_map')

    def execute_command(self, map, pos, command):
        init_pos = copy.deepcopy(pos)
        symbol = map[pos[0], pos[1]]
        new_pos = self.command_impl[command](pos)
        map[*new_pos] = symbol
        map[*init_pos] = '.'
        return map

    def try_execute_command(self, map, robot_pos, command):
        check_pos_queue = [self.command_impl[command](robot_pos)]
        elements_to_move = [robot_pos]
        ends = []
        while True:
            if len(check_pos_queue) == 0: break
            check_pos = check_pos_queue.pop(0)
            if map[*check_pos] == '#': 
                ends.append('#')    # invalidate movement
                break
            elif map[*check_pos] == '.':
                ends.append('.')
            elif map[*check_pos] == 'O':
                elements_to_move.append(check_pos)
                check_pos_queue.append(self.command_impl[command](check_pos))
            elif map[*check_pos] == '[':
                elements_to_move.append(check_pos)
                check_pos_queue.append(self.command_impl[command](check_pos))
                if command == 'v' or command == '^':
                    other_pos = (check_pos[0], check_pos[1]+1)
                    elements_to_move.append(other_pos)
                    check_pos_queue.append(self.command_impl[command](other_pos))
            elif map[*check_pos] == ']':
                elements_to_move.append(check_pos)
                check_pos_queue.append(self.command_impl[command](check_pos))
                if command == 'v' or command == '^':
                    other_pos = (check_pos[0], check_pos[1]-1)
                    elements_to_move.append(other_pos)
                    check_pos_queue.append(self.command_impl[command](other_pos))
        if all([x == '.' for x in ends]):
            # can move!
            # however, invert order: we need to move from 
            # the last element to the first or we would overwrite them
            elements_to_move = elements_to_move[::-1]
            already_moved = set()   # avoid checking same position twice
            for pos in elements_to_move:
                if tuple(pos) not in already_moved:
                    map = self.execute_command(map, pos, command)
                    already_moved.add(tuple(pos))
            robot_pos = self.command_impl[command](robot_pos)
        return map, robot_pos
    
    def compute_gps_coordinates(self, map, box_sprite='O'):
        coords = []
        for y, x in zip(*np.where(map == box_sprite)):
            coords.append(100 * y + x)
        return coords

    def problem_1(self):
        map = copy.deepcopy(self.map)
        robot_pos = [x[0] for x in np.where(map == '@')]
        for command in self.commands:
            map, robot_pos = self.try_execute_command(map, robot_pos, command)
        return sum(self.compute_gps_coordinates(map))
    
    def enlarge_map(self, map):
        orig_shape = map.shape
        new_shape = (orig_shape[0], orig_shape[1] * 2)
        new_map = np.empty(new_shape, dtype='str')
        for y in range(new_shape[0]):
            for x in range(new_shape[1]):
                match map[y, x//2]:
                    case '.': new_map[y, x] = '.'
                    case '#': new_map[y, x] = '#'
                    case 'O': new_map[y, x] = '[' if x % 2 == 0 else ']'
                    case '@': new_map[y, x] = '@' if x % 2 == 0 else '.'
        return new_map
    
    def problem_2(self):
        map = self.enlarge_map(self.map)
        robot_pos = [x[0] for x in np.where(map == '@')]
        for command in self.commands:
            map, robot_pos = self.try_execute_command(map, robot_pos, command)
        return sum(self.compute_gps_coordinates(map, box_sprite='['))
    
if __name__ == '__main__':
    print(Day15())

