"""Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except nums
[i].

Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
    Could you solve it with constant space complexity? (The output array does
    not count as extra space for the purpose of space complexity analysis.)

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        res = []
        size = len(nums)

        for i in range(0, size):
            res.append(p)
            p *= nums[i]

        p = 1
        for i in range(size - 1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res


if __name__ == "__main__":
    s = Solution()

    # Example
    x = [1, 2, 3, 4]
    assert s.productExceptSelf(x) == [24, 12, 8, 6]
