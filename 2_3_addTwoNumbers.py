# -*- coding: utf-8 -*-
# 循环，用空ListNode填充


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node0 = ListNode(val=(l1.val + l2.val))
        result_node, new_node = node0, node0
        while (l1.next is not None) or (l2.next is not None) or (new_node.val > 9):
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            l1_add_l2 = l1.val + l2.val + (1 if new_node.val > 9 else 0)
            new_node.val = new_node.val % 10 if new_node.val > 9 else new_node.val
            new_node.next = ListNode(val=l1_add_l2)
            new_node = new_node.next
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
