# -*- coding: utf-8 -*-
# 逆双指针，不需要创建新数组，结果直接放nums1


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # nums1 = nums1[:m]

        # nums = []
        idx1 = m - 1  # nums1的指针
        idx2 = n - 1  # nums2的指针
        for i in range(1, m + n + 1):  # m+n==len(nums1)
            if idx1 == -1:
                nums1[:idx2 + 1] = nums2[:idx2 + 1]
                break
            if idx2 == -1:
                # nums1[:idx1+1] = nums1[:idx1+1]
                break
            if nums1[idx1] < nums2[idx2]:
                nums1[-i] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[-i] = nums1[idx1]
                idx1 -= 1
        # nums1[:] = nums
        # print(nums1)


if __name__ == '__main__':
    test_nums1 = [1, 2, 7, 9, 0, 0, 0]
    test_m = 4
    test_nums2 = [3, 4, 8]
    test_n = 3

    # test_nums1 = []
    # test_m = 0
    # test_nums2 = [1]
    # test_n = 1

    # test_nums1 = [2, 0]
    # test_m = 1
    # test_nums2 = [1]
    # test_n = 1
    Solution().merge(test_nums1, test_m, test_nums2, test_n)
