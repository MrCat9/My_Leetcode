# -*- coding: utf-8 -*-
# 双指针


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False
        diff_cnt = [0] * 26
        ord_a = ord('a')

        # 计算s1中各个字符的频率
        for i in range(s1_len):
            diff_cnt[ord(s1[i]) - ord_a] -= 1

        left = 0
        for right in range(0, s2_len):
            # 滑动窗口移入x，移出y
            x = ord(s2[right]) - ord_a

            diff_cnt[x] += 1

            while diff_cnt[x] > 0:
                diff_cnt[ord(s2[left]) - ord_a] -= 1
                left += 1

            if right - left + 1 == s1_len:
                return True

        return False


if __name__ == '__main__':
    # test_s1 = 'ab'
    # test_s2 = 'eidbaooo'
    test_s1 = 'ab'
    test_s2 = 'eidboaoo'
    # test_s1 = 'adc'
    # test_s2 = 'dcda'
    Solution().checkInclusion(s1=test_s1, s2=test_s2)
