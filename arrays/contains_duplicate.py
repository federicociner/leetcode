"""Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.

Example 1:

    Input: [1,2,3,1]
    Output: true

Example 2:

    Input: [1,2,3,4]
    Output: false

Example 3:

    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = {}

        for n in nums:
            if n in res.keys():
                return True
            res[n] = True

        return False


if __name__ == "__main__":
    s = Solution()

    # Example 1
    x = [1, 2, 3, 1]
    assert s.containsDuplicate(x) is True

    # Example 2
    y = [1, 2, 3, 4]
    assert s.containsDuplicate(y) is False

    print("All tests passed.")
