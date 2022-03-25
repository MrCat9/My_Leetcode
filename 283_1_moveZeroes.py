# -*- coding: utf-8 -*-
# 倒序循环


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = len_nums - 1
        while i > 0:
            if nums[i] == 0:



        loop_counter = 0
        i = 0
        while loop_counter < len_nums:
            if nums[i] == 0:
                if i + 1 < len_nums:
                    nums[i: len_nums - (i + 1)] = nums[i + 1:]
                    nums[-1] = 0
            else:
                i += 1
            loop_counter += 1
        pass


if __name__ == '__main__':
    test_nums = [0, 1, 0, 3, 12]
    # [1, 3, 12, 0, 0]
    # test_nums = [0]
    # test_nums = [1, 0, 0]
    Solution().moveZeroes(test_nums)
