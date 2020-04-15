"""Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:

    Input: [3,0,1]
    Output: 2

Example 2:

    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

Note:

    Your algorithm should run in linear runtime complexity. Could you
    implement it using only constant extra space complexity?

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        for i, n in enumerate(nums):
            missing ^= i ^ n

        return missing


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert s.missingNumber(nums) == 8

    # Example 2
    nums = [3, 0, 1]
    assert s.missingNumber(nums) == 2

    print("All tests passed.")
