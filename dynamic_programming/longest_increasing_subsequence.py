"""Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

        Input: [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101],
        therefore the length is 4.

Note:

    - There may be more than one LIS combination, it is only necessary for you
    to return the length.
    - Your algorithm should run in O(n ^ 2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

"""
from typing import List


class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # create DP table
        dp = [1] * len(nums)

        # update DP table
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert s.lengthOfLIS(nums) == 4

    # Exampl2 2
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    assert s.lengthOfLIS(nums) == 6
    print("All tests passed.")
