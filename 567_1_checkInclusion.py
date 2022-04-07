# -*- coding: utf-8 -*-
# 滑动窗口


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 超时
        s1_len = len(s1)
        s2_len = len(s2)
        left, right = 0, s1_len
        s1_list = list(s1)

        while right <= s2_len:
            s1l = s1_list.copy()
            sub_s2 = s2[left:right]
            s1_is_sub_s2 = True
            for i, x in enumerate(sub_s2):
                if x in s1l:
                    s1l.remove(x)
                else:
                    s1_is_sub_s2 = False
                    if x not in s1_list:
                        left += (i + 1)
                    else:
                        left += 1
                    right = left + s1_len
                    break
            if s1_is_sub_s2:
                return True
        return False


if __name__ == '__main__':
    # test_s1 = 'ab'
    # test_s2 = 'eidbaooo'
    test_s1 = 'adc'
    test_s2 = 'dcda'
    Solution().checkInclusion(s1=test_s1, s2=test_s2)
