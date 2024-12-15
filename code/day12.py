from collections import defaultdict
import numpy as np

from solution import Solution


class Day12(Solution):
    def __init__(self):
        super().__init__(day=12, year=2024)

    def parse_input(self):
        # self.inp = [
        #     'RRRRIICCFF',
        #     'RRRRIICCCF',
        #     'VVRRRCCFFF',
        #     'VVRCCCJFFF',
        #     'VVVVCJJCFE',
        #     'VVIVCCJJEE',
        #     'VVIIICJJEE',
        #     'MIIIIIJJEE',
        #     'MIIISIJEEE',
        #     'MMMISSJEEE',
        # ]
        return super().parse_input(type='str_map') 
    
    def find_connected_components(self):
        regions = defaultdict(lambda: list())
        for y in range(self.map.shape[0]):
            for x in range(self.map.shape[1]):
                plant = self.map[y, x]
                if y == 0 and x == 0:
                    regions[plant].append({(y, x)})
                else:
                    multi_sub_regions = set(); to_del = []
                    for i, sub_region in enumerate(regions[plant]):
                        if (y-1, x) in sub_region or (y, x-1) in sub_region:
                            multi_sub_regions.update(sub_region)
                            to_del.append(i)
                    # Remove merged regions
                    regions[plant] = [regions[plant][i] 
                                      for i in range(len(regions[plant])) 
                                      if i not in to_del]
                    if len(multi_sub_regions) > 0:
                        multi_sub_regions.update({(y, x)})
                        regions[plant].append(multi_sub_regions)
                    else:
                        regions[plant].append({(y, x)})
        return {
            (str(plant_l), sub_region_id): sub_region
            for plant_l in regions
            for sub_region_id, sub_region in enumerate(regions[plant_l])
        }
    
    def compute_areas(self, conn_map):
        # area is len of each area
        return {
            sub_region: len(conn_map[sub_region])
            for sub_region in conn_map
        }
    
    def compute_perimeters(self, conn_map):
        # each position counts 4 - the number of adjacent positions
        perims = {sub_region: 0 for sub_region in conn_map}
        for sub_region in conn_map:
            for (y, x) in conn_map[sub_region]:
                w_ = 4 - \
                    ((y-1, x) in conn_map[sub_region]) - \
                    ((y+1, x) in conn_map[sub_region]) - \
                    ((y, x-1) in conn_map[sub_region]) - \
                    ((y, x+1) in conn_map[sub_region])
                perims[sub_region] += w_
        return perims
    
    def find_perimeter_positions(self, conn_map):
        # each position counts if it adds at least 1 to the perimeter
        perims = {sub_region: set() for sub_region in conn_map}
        for sub_region in conn_map:
            for (y, x) in conn_map[sub_region]:
                w_ = 4 - \
                    ((y-1, x) in conn_map[sub_region]) - \
                    ((y+1, x) in conn_map[sub_region]) - \
                    ((y, x-1) in conn_map[sub_region]) - \
                    ((y, x+1) in conn_map[sub_region])
                if w_ > 0:
                    perims[sub_region].add((y, x))
        return perims


    def problem_1(self):
        conn_map = self.find_connected_components()
        areas = self.compute_areas(conn_map)
        perimeters = self.compute_perimeters(conn_map)
        return sum([areas[i] * perimeters[i] for i in conn_map])
    
    def problem_2(self):
        conn_map = self.find_connected_components()
        areas = self.compute_areas(conn_map)
        perimeter_positions = self.find_perimeter_positions(conn_map)
        # sides = self.find_sides(perimeter_positions)
        # return sum([areas[i] * sides[i] for i in conn_map])
        return 0
    
if __name__ == '__main__':
    print(Day12())

