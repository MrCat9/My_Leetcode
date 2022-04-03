# -*- coding: utf-8 -*-
# 快慢指针


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    test_nums = [1, 2, 3, 4, 5]
    # test_nums = [1, 2, 3, 4, 5, 6]
    len_test_nums = len(test_nums)

    def gen_list(i):
        if i is not None:
            next_i = i + 1 if i + 1 < len_test_nums else None
            return ListNode(val=test_nums[i], next=gen_list(i=next_i))


    test_head = gen_list(i=0)

    Solution().middleNode(test_head)
