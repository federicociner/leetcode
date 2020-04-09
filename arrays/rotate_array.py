"""Given an array, rotate the array to the right by k steps, where k is
non-negative.

Example 1:

    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]

    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]

    rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

    Input: [-1,-100,3,99] and k = 2
    Output: [3,99,-1,-100]

    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]

Note:

    Try to come up as many solutions as you can, there are at least 3
    different ways to solve this problem.

    Could you do it in-place with O(1) extra space?

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead. """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Example 2
    nums = [-1, -100, 3, 99]
    k = 2
    s.rotate(nums, k)
    assert nums == [3, 99, -1, -100]

    print("All tests passed.")
