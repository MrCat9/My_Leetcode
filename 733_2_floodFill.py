# -*- coding: utf-8 -*-
# 广度优先遍历，用set记录遍历过的点


class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        m = len(image)  # 行
        n = len(image[0])  # 列

        node_list = [(sr, sc)]
        seen_node = set(node_list)
        image[sr][sc] = newColor  # 上色
        while node_list:
            r, c = node_list.pop(0)

            for new_r, new_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # 上下左右
                if 0 <= new_r < m and 0 <= new_c < n and \
                        image[new_r][new_c] == old_color and \
                        (new_r, new_c) not in seen_node:
                    seen_node.add((new_r, new_c))
                    node_list.append((new_r, new_c))
                    image[new_r][new_c] = newColor

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
