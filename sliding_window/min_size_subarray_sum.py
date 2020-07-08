"""Given an array of n positive integers and a positive integer s, find the
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
one, return 0 instead.

Example:

    Input: s = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: the subarray [4,3] has the minimal length under the problem
    constraint.

Follow up:

    If you have figured out the O(n) solution, try coding another solution of
    which the time complexity is O(n log n).

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        curr_sum = 0
        min_len = float("inf")
        left = 0

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= s:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    S = Solution()

    # Example 1
    nums = [2, 3, 1, 2, 4, 3]
    s = 7

    assert S.minSubArrayLen(s, nums) == 2

    print("All tests passed.")
