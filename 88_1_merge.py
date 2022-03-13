# -*- coding: utf-8 -*-
# 双指针


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # nums1 = nums1[:m]

        nums = []
        idx1 = 0  # nums1的指针
        idx2 = 0  # nums2的指针
        for _ in range(m + n):  # m+n==len(nums1)
            if idx1 == m:
                nums += nums2[idx2:n]
                break
            if idx2 == n:
                nums += nums1[idx1:m]
                break
            if nums1[idx1] < nums2[idx2]:
                nums.append(nums1[idx1])
                idx1 += 1
            else:
                nums.append(nums2[idx2])
                idx2 += 1
        nums1[:] = nums
        # print(nums1)


if __name__ == '__main__':
    # test_nums1 = [1, 2, 7, 9, 0, 0, 0]
    # test_m = 4
    # test_nums2 = [3, 4, 8]
    # test_n = 3

    # test_nums1 = []
    # test_m = 0
    # test_nums2 = [1]
    # test_n = 1

    test_nums1 = [2, 0]
    test_m = 1
    test_nums2 = [1]
    test_n = 1
    Solution().merge(test_nums1, test_m, test_nums2, test_n)
