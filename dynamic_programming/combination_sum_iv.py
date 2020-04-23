"""Given an integer array with all positive numbers and no duplicates, find
the number of possible combinations that add up to a positive integer target.

Example:

    nums = [1, 2, 3]
    target = 4

    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)

    Note that different sequences are counted as different combinations.

    Therefore the output is 7.

Follow up:

    What if negative numbers are allowed in the given array?
    How does it change the problem?
    What limitation we need to add to the question to allow negative numbers?

"""
from typing import List


class Solution:
    # Time complexity: O(n * m)
    # Space complexity: O(n)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        dp = [1] + ([0] * target)

        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]


if __name__ == "__main__":
    S = Solution()

    # Example 1
    nums = [1, 2, 3]
    target = 4
    assert S.combinationSum4(nums, target) == 7

    # Example 2
    nums = [1, 2, 3, 4]
    target = 6
    assert S.combinationSum4(nums, target) == 29

    print("All tests passed.")
