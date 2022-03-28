# -*- coding: utf-8 -*-
# 双指针


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        # x + y = target
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:  # sum > target
                right -= 1
        return [None, None]


if __name__ == '__main__':
    test_numbers = [2, 7, 11, 15]
    test_target = 9
    # test_numbers = [-1, 0]
    # test_target = -1
    Solution().twoSum(test_numbers, test_target)
