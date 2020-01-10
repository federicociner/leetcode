"""Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)

        for i in range(size):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(size) if nums[i] > 0]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    x = [4, 3, 2, 7, 8, 2, 3, 1]
    assert s.findDisappearedNumbers(x) == [5, 6]

    # Example 2
    y = [1, 2, 3, 5, 5]
    assert s.findDisappearedNumbers(y) == [4]

    # Example 3
    z = [1, 1]
    assert s.findDisappearedNumbers(z) == [2]

    print("All tests passed.")
