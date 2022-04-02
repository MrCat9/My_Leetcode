# -*- coding: utf-8 -*-
#


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])


if __name__ == '__main__':
    test_s = "Let's take LeetCode contest"  # "s'teL ekat edoCteeL tsetnoc"
    Solution().reverseWords(test_s)


