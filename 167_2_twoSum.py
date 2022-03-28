# -*- coding: utf-8 -*-
# 二分查找


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        # x + y = target
        n = len(numbers)
        for i, x in enumerate(numbers):
            y = target - x
            # 二分查找 y
            left, right = i + 1, n - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == y:
                    return [i + 1, mid + 1]
                elif numbers[mid] < y:
                    left = mid + 1
                else:  # numbers[mid] > y
                    right = mid - 1
        return [None, None]


if __name__ == '__main__':
    test_numbers = [2, 7, 11, 15]
    test_target = 9
    # test_numbers = [-1, 0]
    # test_target = -1
    Solution().twoSum(test_numbers, test_target)
