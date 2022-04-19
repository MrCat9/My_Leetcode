# -*- coding: utf-8 -*-
# 动态规划


class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        nums_sum = sum(nums)
        diff = nums_sum - target
        if diff < 0 or diff % 2 != 0:
            return 0

        n = len(nums)
        neg = diff // 2
        # dp = [[None] * (neg+1)] * (n+1)  # n行neg列
        dp = [[0] * (neg + 1)]  # n+1行neg+1列
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp.append([0] * (neg + 1))
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]

        return dp[n][neg]


if __name__ == '__main__':
    test_nums = [1, 1, 1, 1, 1]
    test_target = 3
    Solution().findTargetSumWays(test_nums, test_target)
