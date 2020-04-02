"""Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1), not including output array
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
            else:
                res.append(abs(n))

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    x = [4, 3, 2, 7, 8, 2, 3, 1]
    assert sorted(s.findDuplicates(x)) == [2, 3]

    # Example 2
    # x = [1, 2, 3, 3, 5, 6, 6, 8]
    # assert sorted(s.findDuplicates(x)) == [3, 6]

    print("All tests passed.")
