# -*- coding: utf-8 -*-
# 双指针， k = lens // 2 + 1 ，找到两个数组中第k大的数 或 第k大和第k-1大


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        m = len(nums1)
        n = len(nums2)
        lens = m + n
        left, right = -1, -1
        idx1, idx2 = 0, 0
        for i in range(lens // 2 + 1):
            left = right
            if idx1 < m and (idx2 >= n or nums1[idx1] < nums2[idx2]):
                right = nums1[idx1]
                idx1 += 1
            else:  # idx1 >= m or (idx2 < n and nums1[idx1] >= nums2[idx2])
                right = nums2[idx2]
                idx2 += 1

        if (lens & 1) == 0:
            return (left + right) / 2
        else:
            return right


if __name__ == '__main__':
    # test_nums1 = [1, 3]
    # test_nums2 = [2]

    # test_nums1 = [1, 2]
    # test_nums2 = [3, 4]

    # test_nums1 = [1, 3, 4]
    # test_nums2 = [2, 7, 8]

    # test_nums1 = [2, 3, 5, 6, 7]
    # test_nums2 = [1, 4]

    # test_nums1 = [2, 3, 5, 6, 7]
    # test_nums2 = [8, 9]

    test_nums1 = [1, 2, 7, 9]
    test_nums2 = [3, 4, 8]

    # test_nums1 = [2]
    # test_nums2 = [1]

    test_result = Solution().findMedianSortedArrays(test_nums1, test_nums2)
    print(test_result)
