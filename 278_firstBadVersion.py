# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# 二分查找


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        while left < right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        # left >= right
        return left


if __name__ == '__main__':
    test_n = 8
    test_bad = 4

    def isBadVersion(version):
        return version >= test_bad

    test_result = Solution().firstBadVersion(test_n)
    print(test_result)
