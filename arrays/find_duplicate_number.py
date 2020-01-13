"""Given an nums nums containing n + 1 integers where each integer is between
1 and n (inclusive), prove that at least one duplicate number must exist.

Assume that there is only one duplicate number, find the duplicate one.

Example 1:

    Input: [1,3,4,2,2]
    Output: 2

Example 2:

    Input: [3,1,3,4,2]
    Output: 3

Note:

    - You must not modify the nums (assume the nums is read only).
    - You must use only constant, O(1) extra space.
    - Your runtime complexity should be less than O(n2).
    - There is only one duplicate number in the nums, but it could be repeated
    more than once.

"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    s = Solution()

    # # Example 1
    x = [1, 3, 4, 2, 2]
    assert s.findDuplicate(x) == 2

    # Example 2
    y = [3, 1, 3, 4, 2]
    assert s.findDuplicate(y) == 3
