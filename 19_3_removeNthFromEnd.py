# -*- coding: utf-8 -*-
# 哑节点 + 双指针


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # 哑节点

        first = head  # 第一个指针用来遍历链表
        second = dummy  # 第二个指针指向要删除节点的上一个节点

        # first 与 second 相差 n
        for _ in range(n):
            first = first.next

        # first 遍历到链表结束
        while first:
            first = first.next
            second = second.next

        # 删除节点
        second.next = second.next.next

        return dummy.next


if __name__ == '__main__':
    test_nums = [1, 2, 3, 4, 5]
    test_n = 2
    # test_nums = [1]
    # test_n = 1
    # test_nums = [1, 2]
    # test_n = 1
    len_test_nums = len(test_nums)


    def gen_list(i):
        if i is not None:
            next_i = i + 1 if i + 1 < len_test_nums else None
            return ListNode(val=test_nums[i], next=gen_list(i=next_i))


    test_head = gen_list(i=0)

    Solution().removeNthFromEnd(test_head, test_n)
