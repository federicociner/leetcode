"""Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

    If you have figured out the O(n) solution, try coding another solution
    using the divide and conquer approach, which is more subtle.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) < 2:
            return nums[0]

        # initialize DP table
        dp = [0] * len(nums)

        # base case
        dp[0] = nums[0]

        # populate DP table
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])

        return max(dp)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert s.maxSubArray(nums) == 6

    print("All tests passed.")
