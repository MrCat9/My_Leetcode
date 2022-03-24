# -*- coding: utf-8 -*-
# 双指针，逆序


class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        len_nums = len(nums)
        i1 = 0
        i2 = len_nums - 1
        result_nums = []
        while i1 <= i2:
            # if abs(nums[i1]) < abs(nums[i2]):
            if -nums[i1] < nums[i2]:
                result_nums.append(nums[i2] * nums[i2])
                i2 -= 1
            else:
                result_nums.append(nums[i1] * nums[i1])
                i1 += 1

        return result_nums[::-1]


if __name__ == '__main__':
    # test_nums = [-4, -1, 0, 3, 10]
    # test_nums = [-7, -3, 2, 3, 11]
    # test_nums = [1, 2, 3, 4, 5]
    test_nums = [-5, -4, -3, -2, -1]

    test_result = Solution().sortedSquares(test_nums)
    # print(test_result)
