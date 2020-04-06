"""Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m
+ n) to hold additional elements from nums2.

Example:

    Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]

"""
from typing import List


class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(m)
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        m = m - 1
        n = n - 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m + n + 1] = nums1[m]
                m -= 1
            else:
                nums1[m + n + 1] = nums2[n]
                n -= 1

        if n != -1:
            nums1[: n + 1] = nums2[: n + 1]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    expected = [1, 2, 2, 3, 5, 6]
    s.merge(nums1, 3, nums2, 3)
    assert nums1 == expected

    # Example 2
    nums1 = [1, 2, 3, 3, 4, 8, 0, 0, 0, 0]
    nums2 = [2, 4, 5, 7]
    expected = [1, 2, 2, 3, 3, 4, 4, 5, 7, 8]
    s.merge(nums1, 6, nums2, 4)
    assert nums1 == expected

    print("All tests passed.")
