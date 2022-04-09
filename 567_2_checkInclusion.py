# -*- coding: utf-8 -*-
# 滑动窗口 优化
# 使用diff，不比较整个cnt1和cnt2数组


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False
        diff_cnt = [0] * 26
        ord_a = ord('a')

        # 计算s1和s2中各个字符频率的差
        for i in range(s1_len):
            diff_cnt[ord(s1[i]) - ord_a] -= 1
            diff_cnt[ord(s2[i]) - ord_a] += 1

        diff = 0  # 错误的位数
        # diff = sum([bool(i) for i in diff_cnt])
        for i in diff_cnt:
            if i:
                diff += 1
        if diff == 0:
            return True

        for i2 in range(s1_len, s2_len):
            # 滑动窗口移入x，移出y
            x = ord(s2[i2]) - ord_a
            y = ord(s2[i2 - s1_len]) - ord_a

            if x == y:
                continue

            if diff_cnt[x] == 0:
                diff += 1
            diff_cnt[x] += 1
            if diff_cnt[x] == 0:
                diff -= 1

            if diff_cnt[y] == 0:
                diff += 1
            diff_cnt[y] -= 1
            if diff_cnt[y] == 0:
                diff -= 1

            if diff == 0:
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
