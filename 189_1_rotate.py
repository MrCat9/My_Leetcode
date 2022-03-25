# -*- coding: utf-8 -*-
# 数组翻转


class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        nums.reverse()  # reverse 比 [::-1] 快
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


if __name__ == '__main__':
    test_nums = [1, 2, 3, 4, 5, 6, 7]
    test_k = 3
    # [5, 6, 7, 1, 2, 3, 4]

    Solution().rotate(test_nums, test_k)
