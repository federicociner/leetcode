"""You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed. All houses at this place are
arranged in a circle. That means the first house is the neighbor of the last
one. Meanwhile, adjacent houses have security system connected and it will
automatically contact the police if two adjacent houses were broken into on
the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

Example 1:

    Input: [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3
    (money = 2), because they are adjacent houses.

Example 2:

    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0:2])

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [2, 3, 2]
    assert s.rob(nums) == 3

    # Example 2
    nums = [1, 2, 3, 1]
    assert s.rob(nums) == 4

    # Example 3
    nums = [1, 2, 1, 1]
    assert s.rob(nums) == 3

    print("All tests passed.")
