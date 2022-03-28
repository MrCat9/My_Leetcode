# -*- coding: utf-8 -*-
# 哈希表


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        if target > sum(numbers[-2:]) or target < sum(numbers[:2]):
            return [None, None]

        # x + y = target
        y_index_dict = {}
        for i, x in enumerate(numbers):
            y = target - x
            if x in y_index_dict:
                return [y_index_dict[x] + 1, i + 1]
            else:
                y_index_dict[y] = i
        return [None, None]


if __name__ == '__main__':
    # test_numbers = [2, 7, 11, 15]
    # test_target = 9
    test_numbers = [-1, 0]
    test_target = -1
    Solution().twoSum(test_numbers, test_target)
