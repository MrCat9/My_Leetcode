# -*- coding: utf-8 -*-
# 深度优先，访问过的置0


class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        m = len(grid)  # 行
        n = len(grid[0])  # 列
        max_area = 0

        def get_island_area(sx, sy):  # DFS
            grid[sy][sx] = 0
            ia = 1
            for new_x, new_y in [(sx - 1, sy), (sx + 1, sy), (sx, sy - 1), (sx, sy + 1)]:
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_y][new_x] == 1:
                    grid[new_y][new_x] = 0  # 置0
                    ia += get_island_area(new_x, new_y)
            return ia

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
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
