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
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        end = p1 + p2
        if p1 < m:
            nums1[end:] = nums1_copy[p1:]

        if p2 < n:
            nums1[end:] = nums2[p2:]


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
