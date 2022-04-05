# -*- coding: utf-8 -*-
# 哑节点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # 哑节点
        len_sl = 0  # 链表长度
        curr_node = dummy
        previous_rm_node = None  # 要删除节点的上一个节点
        n += 1  # 要删除节点的上一个节点是倒数n+1

        # 找到 previous_rm_node
        while curr_node:
            len_sl += 1
            if len_sl == n:
                previous_rm_node = dummy
            elif len_sl > n:
                previous_rm_node = previous_rm_node.next
            curr_node = curr_node.next

        # 删除节点
        if previous_rm_node:
            previous_rm_node.next = previous_rm_node.next.next

        return dummy.next


if __name__ == '__main__':
    # test_nums = [1, 2, 3, 4, 5]
    # test_n = 5
    test_nums = [1]
    test_n = 1
    # test_nums = [1, 2]
    # test_n = 1
    len_test_nums = len(test_nums)


    def gen_list(i):
        if i is not None:
            next_i = i + 1 if i + 1 < len_test_nums else None
            return ListNode(val=test_nums[i], next=gen_list(i=next_i))


    test_head = gen_list(i=0)

    Solution().removeNthFromEnd(test_head, test_n)
