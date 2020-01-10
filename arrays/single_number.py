"""Given a non-empty array of integers, every element appears twice except for
one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Example 1:

    Input: [2,2,1]
    Output: 1

Example 2:

    Input: [4,1,2,1,2]
    Output: 4

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    x = [2, 2, 1]
    assert s.singleNumber(x) == 1

    # Example 2
    y = [4, 1, 2, 1, 2]
    assert s.singleNumber(y) == 4

    print("All tests passed.")
