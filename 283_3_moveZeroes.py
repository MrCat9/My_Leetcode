# -*- coding: utf-8 -*-
# 双指针


class Solution:
    # def moveZeroes(self, nums: [int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     len_nums = len(nums)
    #     j = 0  # 填入非0数字的位置
    #     for i in range(len_nums):
    #         if nums[i] != 0:
    #             nums[j], nums[i] = nums[i], nums[j]
    #             j += 1

    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        j = 0  # 填入非0数字的位置
        for i in range(len_nums):
            if nums[i] != 0:
                if i > j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1


if __name__ == '__main__':
    test_nums = [1, 0, 0, 3, 4]  # [1, 3, 12, 0, 0]
    # test_nums = [0]
    # test_nums = [1]
    # test_nums = [1, 0, 0]
    Solution().moveZeroes(test_nums)
