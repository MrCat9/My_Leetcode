# -*- coding: utf-8 -*-
# 类型转换


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        def list2int(lst: list) -> int:
            lst = lst[::-1]
            lst = [str(n) for n in lst]
            lst = ''.join(lst)
            return int(lst)

        i1 = list2int(l1)
        i2 = list2int(l2)
        sum_str = str(i1 + i2)
        sum_list = [i for i in sum_str]
        sum_list = sum_list[::-1]
        return sum_list


if __name__ == '__main__':
    # test_l1 = [2, 4, 3]
    # test_l2 = [5, 6, 4]

    test_l1 = [9, 9, 9, 9, 9, 9, 9]
    test_l2 = [9, 9, 9, 9]

    test_result = Solution().addTwoNumbers(l1=test_l1, l2=test_l2)
    print(test_result)
