"""Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        while low < high:
            mid = int((high + low) / 2)

            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid
                else:
                    return mid
            elif target < nums[0]:
                low = mid + 1
            else:
                high = mid

        if nums[low] == target:
            return low

        return -1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    x = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert s.search(x, target) == 4

    # Example 2
    y = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert s.search(y, target) == -1

    # Example 3
    z = [1]
    target = 1
    assert s.search(z, target) == 0

    # Example 4
    a = [1, 3]
    target = 3
    assert s.search(a, target) == 1
