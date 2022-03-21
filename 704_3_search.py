# -*- coding: utf-8 -*-
# 二分查找，下标截取


class Solution:
    def search(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:  # nums[mid] > target
                right = mid - 1
        return -1


if __name__ == '__main__':
    test_nums = [-1, 0, 3, 5, 9, 12, 13]
    # test_target = 9
    test_target = 2

    test_result = Solution().search(test_nums, test_target)
    print(test_result)
