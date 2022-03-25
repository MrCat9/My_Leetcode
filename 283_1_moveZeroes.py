# -*- coding: utf-8 -*-
# 倒序循环


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = len_nums - 2  # 从倒数第二个开始，最后一个不用判断
        first0flag = True  # 第一次看到0
        while i >= 0:
            if nums[i] == 0:
                nums[i: len_nums - 1] = nums[i + 1: len_nums]  # 很慢
                if first0flag:
                    nums[-1] = 0
                    first0flag = False
            i -= 1


if __name__ == '__main__':
    test_nums = [0, 0, 0, 3, 4]
    # [1, 3, 12, 0, 0]
    # test_nums = [0]
    # test_nums = [1, 0, 0]
    Solution().moveZeroes(test_nums)
