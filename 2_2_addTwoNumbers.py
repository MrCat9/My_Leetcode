# -*- coding: utf-8 -*-
# 递归


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, up_flag=False) -> ListNode:
        result_node = ListNode()

        if up_flag:
            l1_add_l2 = l1.val + l2.val + 1
            up_flag = False
        else:
            l1_add_l2 = l1.val + l2.val

        if l1_add_l2 // 10 == 1:
            up_flag = True
            l1_add_l2 = l1_add_l2 % 10
        result_node.val = l1_add_l2

        next_l1 = l1.next if l1.next else ListNode()
        next_l2 = l2.next if l2.next else ListNode()
        if up_flag or l1.next or l2.next:
            result_node.next = self.addTwoNumbers(l1=next_l1, l2=next_l2, up_flag=up_flag)

        return result_node


if __name__ == '__main__':
    def list2list_node(lst: list, i=0) -> ListNode:
        node = ListNode()
        node.val = lst[i]
        i += 1
        if i < len(lst):
            node.next = list2list_node(lst, i)
        # else:
        #     node.next = None
        return node

    # test_l1 = [2, 4, 3]
    # test_l2 = [5, 6, 4]
    test_l1 = [9, 9, 9, 9, 9, 9, 9]
    test_l2 = [9, 9, 9, 9]
    test_l1 = list2list_node(test_l1)
    test_l2 = list2list_node(test_l2)

    test_result = Solution().addTwoNumbers(l1=test_l1, l2=test_l2)
    print(test_result)
