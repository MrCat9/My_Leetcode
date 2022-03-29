# -*- coding: utf-8 -*-
#


class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[:] = s[::-1]
        s.reverse()


if __name__ == '__main__':
    test_s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(test_s)
