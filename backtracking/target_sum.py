"""You are given a list of non-negative integers, a1, a2, ..., an, and a
target, S. Now you have 2 symbols + and -. For each integer, you should choose
one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to
target S.

Example 1:

    Input: nums is [1, 1, 1, 1, 1], S is 3.
    Output: 5

    Explanation:

    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

    There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
    - The length of the given array is positive and will not exceed 20.
    - The sum of elements in the given array will not exceed 1000.
    - Your output answer is guaranteed to be fitted in a 32-bit integer.

"""
from typing import List
from collections import defaultdict


class Solution:
    # Time complexity: O(nk)
    # Space complexity: O(n)
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0

        prev = defaultdict(int)

        # base case
        prev[nums[0]] += 1
        prev[-nums[0]] += 1

        for i in range(1, len(nums)):
            temp = defaultdict(int)

            for k, v in prev.items():
                temp[k + nums[i]] += v
                temp[k - nums[i]] += v

            prev = temp

        return prev[S]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    assert s.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5

    print("All tests passed.")
