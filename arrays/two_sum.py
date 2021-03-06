"""Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            x = target - n

            if x in d:
                return [d[x], i]

            d[n] = i

        return [-1, -1]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [2, 7, 11, 15]
    target = 22
    res = s.twoSum(nums, target)

    assert nums[res[0]] + nums[res[1]] == target

    # Example 2
    nums = [5, 9, 23, 6]
    target = 28
    res = s.twoSum(nums, target)

    assert nums[res[0]] + nums[res[1]] == target

    print("All tests passed.")
