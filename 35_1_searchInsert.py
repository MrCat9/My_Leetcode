# -*- coding: utf-8 -*-
# 二分查找


class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    test_nums = [1, 3, 5, 6]
    # test_target = 5
    # test_target = 2
    test_target = 7

    test_result = Solution().searchInsert(test_nums, test_target)
    print(test_result)
