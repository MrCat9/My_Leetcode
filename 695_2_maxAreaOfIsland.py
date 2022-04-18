# -*- coding: utf-8 -*-
# 广度优先，访问过的置0


class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        m = len(grid)  # 行
        n = len(grid[0])  # 列
        max_area = 0
        # seen_set = set()

        def get_island_area(sx, sy):  # BFS
            grid[sy][sx] = 0
            ia = 1
            i_list = [(sx, sy)]
            while i_list:
                _x, _y = i_list.pop(0)
                for new_x, new_y in [(_x - 1, _y), (_x + 1, _y), (_x, _y - 1), (_x, _y + 1)]:
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_y][new_x] == 1:
                        # seen_set.add((new_x, new_y))
                        grid[new_y][new_x] = 0  # 置0
                        i_list.append((new_x, new_y))
                        ia += 1
            return ia

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                # if (x, y) in seen_set:
                #     continue
                # seen_set.add((x, y))
                if cell == 0:
                    continue
                else:
                    max_area = max(get_island_area(x, y), max_area)

        return max_area


if __name__ == '__main__':
    test_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    Solution().maxAreaOfIsland(grid=test_grid)
