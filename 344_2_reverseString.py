# -*- coding: utf-8 -*-
# 双指针


class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        times = len(s) // 2
        left = times - 1
        if len(s) % 2 == 0:  # 偶数
            right = times
        else:
            right = times + 1

        for _ in range(times):
            s[left], s[right] = s[right], s[left]
            left -= 1
            right += 1


if __name__ == '__main__':
    test_s = ["h", "e", "l", "l", "o"]
    # test_s = ["h", "e", "l", "l"]
    Solution().reverseString(test_s)
