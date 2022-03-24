# -*- coding: utf-8 -*-
# 暴力法


class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        return sorted([x * x for x in nums])


if __name__ == '__main__':
    test_nums = [-4, -1, 0, 3, 10]

    test_result = Solution().sortedSquares(test_nums)
    # print(test_result)
