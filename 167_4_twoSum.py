# -*- coding: utf-8 -*-
# 双指针 + 二分查找


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        # x + y = target
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2

            if numbers[left] + numbers[mid] > target:
                right = mid - 1
            # elif numbers[left] + numbers[mid] < target:
            #     pass

            elif numbers[mid] + numbers[right] < target:
                left = mid + 1
            # elif numbers[mid] + numbers[right] > target:
            #     pass

            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1

            else:
                return [left + 1, right + 1]

        return [None, None]


if __name__ == '__main__':
    # test_numbers = [2, 7, 11, 15]
    # test_target = 9
    test_numbers = [-1, 0]
    test_target = -1
    Solution().twoSum(test_numbers, test_target)
