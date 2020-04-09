"""Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead. """
        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            if nums[slow] != 0:
                slow += 1

            fast += 1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    # Example 2
    nums = [0, 0, 0, 3, 12, 5, 0, 3]
    s.moveZeroes(nums)
    assert nums == [3, 12, 5, 3, 0, 0, 0, 0]

    print("All tests passed.")
