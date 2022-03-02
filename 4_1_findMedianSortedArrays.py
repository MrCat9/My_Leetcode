# -*- coding: utf-8 -*-
# 合并数组，排序，计算中位数（暴力求解）


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        nums12 = nums1 + nums2
        nums12.sort()
        nums12_len = len(nums12)
        if nums12_len % 2 == 1:  # 长度为奇数
            return nums12[nums12_len // 2]
        else:
            return (nums12[nums12_len // 2 - 1] + nums12[nums12_len // 2]) / 2


if __name__ == '__main__':
    # test_nums1 = [1, 3]
    # test_nums2 = [2]

    test_nums1 = [1, 2]
    test_nums2 = [3, 4]

    test_result = Solution().findMedianSortedArrays(test_nums1, test_nums2)
    print(test_result)
