"""Given an array of size n, find the majority element. The majority element
is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.

Example 1:

    Input: [3,2,3]
    Output: 3

Example 2:

    Input: [2,2,1,1,1,2,2]
    Output: 2

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1

        return candidate


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [3, 2, 3]
    expected = 3
    assert s.majorityElement(nums) == expected

    # Example 2
    nums = [2, 2, 1, 1, 1, 2, 2]
    expected = 2
    assert s.majorityElement(nums) == expected

    print("All tests passed.")
