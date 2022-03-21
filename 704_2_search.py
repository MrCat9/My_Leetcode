# -*- coding: utf-8 -*-
# 二分查找，列表截取


class Solution:
    def search(self, nums: [int], target: int) -> int:
        tmp_nums = nums.copy()
        while tmp_nums:
            i = len(tmp_nums) // 2
            if tmp_nums[i] > target:
                tmp_nums = tmp_nums[:i]
            elif tmp_nums[i] < target:
                tmp_nums = tmp_nums[i + 1:]
            else:
                return nums.index(tmp_nums[i])
        return -1


if __name__ == '__main__':
    test_nums = [-1, 0, 3, 5, 9, 12, 13]
    # test_target = 9
    test_target = 2

    test_result = Solution().search(test_nums, test_target)
    print(test_result)
