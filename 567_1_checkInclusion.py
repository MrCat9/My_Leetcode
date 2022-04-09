# -*- coding: utf-8 -*-
# 滑动窗口
# 由于排列不会改变字符串中每个字符的个数，所以只有当两个字符串每个字符的个数均相等时，一个字符串才是另一个字符串的排列。


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        ord_a = ord('a')

        # 计算s1和s2中各个字符的频率
        for i in range(s1_len):
            cnt1[ord(s1[i]) - ord_a] += 1
            cnt2[ord(s2[i]) - ord_a] += 1
        if cnt1 == cnt2:
            return True

        for i2 in range(s1_len, s2_len):
            # 计算s2中各个字符的频率
            cnt2[ord(s2[i2]) - ord_a] += 1
            cnt2[ord(s2[i2 - s1_len]) - ord_a] -= 1

            if cnt1 == cnt2:
                return True

        return False


if __name__ == '__main__':
    # test_s1 = 'ab'
    # test_s2 = 'eidbaooo'
    test_s1 = 'adc'
    test_s2 = 'dcda'
    Solution().checkInclusion(s1=test_s1, s2=test_s2)
