# -*- coding: utf-8 -*-
# 动态规划，滚动数组优化空间复杂度


class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        nums_sum = sum(nums)
        diff = nums_sum - target
        if diff < 0 or diff % 2:
            return 0

        # n = len(nums)
        neg = diff // 2
        # dp = [[None] * (neg+1)] * (n+1)  # n行neg列
        dp = [0] * (neg + 1)  # 1行neg+1列
        dp[0] = 1

        for num in nums:
            # for j in range(neg, -1, -1):
            #     if j >= num:
            #         dp[j] += dp[j - num]
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]

        # return dp[neg]
        return dp[-1]


if __name__ == '__main__':
    test_nums = [1, 1, 1, 1, 1]
    test_target = 3
    Solution().findTargetSumWays(test_nums, test_target)
