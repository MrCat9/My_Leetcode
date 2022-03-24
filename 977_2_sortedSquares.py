# -*- coding: utf-8 -*-
# 双指针


class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        abs_nums = [abs(x) for x in nums]
        min_num = min(abs_nums)
        min_num_i = abs_nums.index(min_num)
        nums1 = abs_nums[:min_num_i][::-1]
        nums2 = abs_nums[min_num_i + 1:] if min_num_i + 1 < len(nums) else []
        nums1 = [x * x for x in nums1]
        nums2 = [x * x for x in nums2]
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        i1 = 0
        i2 = 0
        result_nums = [min_num * min_num]
        while i1 <= len_nums1 and i2 <= len_nums2:
            if i1 == len_nums1:
                result_nums += nums2[i2:]
                break
            if i2 == len_nums2:
                result_nums += nums1[i1:]
                break
            if nums1[i1] < nums2[i2]:
                result_nums.append(nums1[i1])
                i1 += 1
            else:
                result_nums.append(nums2[i2])
                i2 += 1

        return result_nums


if __name__ == '__main__':
    # test_nums = [-4, -1, 0, 3, 10]
    # test_nums = [-7, -3, 2, 3, 11]
    # test_nums = [1, 2, 3, 4, 5]
    test_nums = [-5, -4, -3, -2, -1]

    test_result = Solution().sortedSquares(test_nums)
    print(test_result)
