# -*- coding: utf-8 -*-
# 二分法


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        max_num = 1000000
        min_num = -1000000

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        nums_len = nums1_len + nums2_len
        is_odd = True if nums_len % 2 == 1 else False

        # 让nums1比nums2长或相等
        if nums1_len < nums2_len:
            nums1, nums2 = nums2, nums1
            nums1_len, nums2_len = nums2_len, nums1_len

        left_nums_len = (nums_len + 1) // 2
        nums1_line = left_nums_len - 1  # nums1_line起始位置
        nums2_line = -1  # nums2_line起始位置

        # 寻找分割线
        # is_find_line = False
        while nums1_line >= -1 and nums2_line < nums2_len:
            # 得到2条分割线两端的4个数
            nums1_line_left = nums1[nums1_line] if nums1_line > -1 else (min_num - 1)
            nums1_line_right = nums1[nums1_line + 1] if nums1_line + 1 < nums1_len else (max_num + 1)
            nums2_line_left = nums2[nums2_line] if nums2_line > -1 else (min_num - 1)
            nums2_line_right = nums2[nums2_line + 1] if nums2_line + 1 < nums2_len else (max_num + 1)

            # 调整分割线位置
            if nums1_line_left > nums2_line_right:
                nums1_line -= 1  # nums1_line左移
                nums2_line += 1
            # elif nums1_line_right < nums2_line_left:
            #     nums1_line += 1  # nums1_line右移
            #     nums2_line -= 1
            else:
                # is_find_line = True
                break

        # if not is_find_line:
        #     raise Exception('not find line')

        # 得到中位数
        if is_odd:
            return max(nums1_line_left, nums2_line_left)
        else:
            return (max(nums1_line_left, nums2_line_left) + min(nums1_line_right, nums2_line_right)) / 2


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

    # test_nums1 = [1, 2, 7, 9]
    # test_nums2 = [3, 4, 8]

    test_nums1 = [2]
    test_nums2 = [1]

    test_result = Solution().findMedianSortedArrays(test_nums1, test_nums2)
    print(test_result)
