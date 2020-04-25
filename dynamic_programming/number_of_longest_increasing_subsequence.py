"""Given an unsorted array of integers, find the number of longest increasing
subsequence.

Example 1:

    Input: [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and
    [1, 3, 5, 7].

Example 2:

    Input: [2,2,2,2,2]
    Output: 5
    Explanation: The length of longest continuous increasing subsequence is 1,
    and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is
guaranteed to be fit in 32-bit signed int.

"""
from typing import List


class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        dp = [1] * n
        lis = [1] * n

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue

                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    lis[i] = lis[j]
                elif dp[j] + 1 == dp[i]:
                    lis[i] += lis[j]

        max_len = max(dp)
        count = sum([lis[i] for i in range(len(nums)) if max_len == dp[i]])

        return count


if __name__ == "__main__":
    S = Solution()

    # Example 1
    nums = [1, 3, 5, 4, 7]
    assert S.findNumberOfLIS(nums) == 2

    # Example 2
    nums = [2, 2, 2, 2, 2]
    assert S.findNumberOfLIS(nums) == 5

    # Example 3
    nums = [1, 2, 4, 3, 5, 4, 7, 2]
    assert S.findNumberOfLIS(nums) == 3

    print("All tests passed.")
