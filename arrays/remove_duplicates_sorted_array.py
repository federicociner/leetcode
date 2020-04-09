"""Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of
    nums being 1 and 2 respectively.

Example 2:

    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of
    nums being modified to 0, 1, 2, 3, and 4 respectively.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        j = 0

        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                i += 1
            else:
                i += 1

        return j + 1


if __name__ == "__main__":
    s = Solution()

    # Example
    x = [1, 1, 2]
    assert s.removeDuplicates(x) == 2
    assert x[:2] == [1, 2]

    # Example 2
    x = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert s.removeDuplicates(x) == 5
    assert x[:5] == [0, 1, 2, 3, 4]

    print("All tests passed.")
