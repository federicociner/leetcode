"""Given an integer array nums, find the sum of the elements between indices i
and j (i ≤ j), inclusive.

Example:

    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.

"""
from typing import List


class NumArray:
    # Time complexity: O(1)
    # Space complexity: O(n)
    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.sums[i + 1] = self.sums[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    s = NumArray(nums)

    # Example 1
    assert s.sumRange(0, 2) == 1
    assert s.sumRange(2, 5) == -1
    assert s.sumRange(0, 5) == -3

    print("All tests passed.")
