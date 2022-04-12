# -*- coding: utf-8 -*-
# 深度优先遍历


class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        old_color = image[sr][sc]
        m = len(image)  # 行
        n = len(image[0])  # 列

        def dfs(r: int, c: int):
            # if image[r][c] == old_color:
            image[r][c] = newColor  # 上色
            for new_r, new_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # 上下左右
                if 0 <= new_r < m and 0 <= new_c < n and \
                        image[new_r][new_c] == old_color:
                    dfs(new_r, new_c)

        if old_color != newColor:
            dfs(sr, sc)
        return image


if __name__ == '__main__':
    test_image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    test_sr = 1
    test_sc = 1
    test_newColor = 2
    # test_image = [[0, 0, 0], [0, 1, 1]]
    # test_sr = 1
    # test_sc = 1
    # test_newColor = 1
    Solution().floodFill(image=test_image, sr=test_sr, sc=test_sc, newColor=test_newColor)
