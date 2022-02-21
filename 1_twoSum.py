# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        tmp_dict = {}
        # tmp_dict = {
        #     num_supp: num_index
        # }
        # num + num_supp = target
        for num_index, num in enumerate(nums):
            if num in tmp_dict:
                return [num_index, tmp_dict[num]]
            num_supp = target - num
            if num_supp not in tmp_dict:
                tmp_dict[num_supp] = num_index
        return []


if __name__ == '__main__':
    test_nums = [2, 7, 11, 15]
    test_target = 9
    test_result = Solution().twoSum(nums=test_nums, target=test_target)
    print(test_result)
