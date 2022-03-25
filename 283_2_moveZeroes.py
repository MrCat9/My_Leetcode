# -*- coding: utf-8 -*-
# 双指针


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        j = 0  # 填入非0数字的位置
        for i in range(len_nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        if j < len_nums:
            nums[j:] = [0] * (len_nums - j)


if __name__ == '__main__':
    test_nums = [1, 0, 0, 3, 4]  # [1, 3, 12, 0, 0]
    # test_nums = [0]
    # test_nums = [1]
    # test_nums = [1, 0, 0]
    Solution().moveZeroes(test_nums)
