"""Given an array of integers A sorted in non-decreasing order, return an
array of the squares of each number, also in sorted non-decreasing order.



Example 1:

    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

Example 2:

    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]


Note:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []

        res = [0] * len(A)
        left = 0
        right = len(A) - 1

        while left <= right:
            left_val = abs(A[left])
            right_val = abs(A[right])
            if left_val > right_val:
                res[right - left] = left_val ** 2
                left += 1
            else:
                res[right - left] = right_val ** 2
                right -= 1

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    A = [-4, -1, 0, 3, 10]
    expected = [0, 1, 9, 16, 100]
    actual = s.sortedSquares(A)

    assert actual == expected

    # Example 2
    B = [-7, -3, 2, 3, 11]
    expected = [4, 9, 9, 49, 121]
    actual = s.sortedSquares(B)

    assert actual == expected
