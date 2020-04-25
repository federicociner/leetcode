"""Given a non-empty array containing only positive integers, find if the
array can be partitioned into two subsets such that the sum of elements in
both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

    Input: [1, 2, 3, 5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.

"""
from typing import List


class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n ^ 2)
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        target = sum(nums)

        if target % 2 > 0:
            return False

        target //= 2

        # initialize DP table
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # base cases
        dp[0][0] = True

        for row in range(1, n + 1):
            dp[row][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]

                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]


if __name__ == "__main__":
    S = Solution()

    # Example 1
    nums = [1, 5, 11, 5]
    assert S.canPartition(nums) is True

    # Example 2
    nums = [1, 2, 3, 5]
    assert S.canPartition(nums) is False

    print("All tests passed.")
