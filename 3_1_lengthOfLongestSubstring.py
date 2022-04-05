# -*- coding: utf-8 -*-
# 滑动窗口


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        curr_s = ''
        curr_s_len = 0
        for i, c in enumerate(s):
            if c not in curr_s:
                curr_s += c
                curr_s_len += 1
            else:  # 重复时
                # 上一子串结束，输出上一子串长度
                if curr_s_len > max_len:
                    max_len = curr_s_len
                # 更新下一子串
                csci = curr_s.find(c)  # 重复的位置
                curr_s = curr_s[csci + 1:]  # 字符串分割
                curr_s += c
                # curr_s_len = curr_s_len - csci - 1  # 分割后的长度
                # curr_s_len += 1
                curr_s_len = curr_s_len - csci  # -1和+1抵消
        if curr_s_len > max_len:  # 若最长无重复子串在最后
            max_len = curr_s_len
        return max_len


if __name__ == '__main__':
    test_s = 'abcabcbb'
    # test_s = 'abcbdabb'
    # test_s = 'bbbbb'
    # test_s = 'pwwkew'
    # test_s = 'pwwkeabc'
    # test_s = ''
    test_result = Solution().lengthOfLongestSubstring(test_s)
    print(test_result)
