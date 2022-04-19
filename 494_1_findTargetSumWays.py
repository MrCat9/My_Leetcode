# -*- coding: utf-8 -*-
# 回溯


class Solution:
    ways = 0

    def findTargetSumWays(self, nums: [int], target: int) -> int:
        n = len(nums)

        def backtrack(curr_sum: int, idx: int):
            if idx == n:
                if curr_sum == target:
                    self.ways += 1
            else:
                backtrack(curr_sum=curr_sum + nums[idx], idx=idx + 1)
                backtrack(curr_sum=curr_sum - nums[idx], idx=idx + 1)

        backtrack(curr_sum=0, idx=0)
        return self.ways


if __name__ == '__main__':
    test_nums = [1, 1, 1, 1, 1]
    test_target = 3
    Solution().findTargetSumWays(test_nums, test_target)
