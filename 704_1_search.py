# -*- coding: utf-8 -*-
# list.index


class Solution:
    def search(self, nums: [int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


if __name__ == '__main__':
    test_nums = [-1, 0, 3, 5, 9, 12, 13]
    # test_target = 9
    test_target = 2

    test_result = Solution().search(test_nums, test_target)
    print(test_result)
