"""Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:

    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(3n)
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) < 1:
            return nums[0]

        # initialize DP tables
        local_min = [0] * len(nums)
        local_max = [0] * len(nums)

        # base cases
        local_min[0] = nums[0]
        local_max[0] = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                local_max[i] = max(local_min[i - 1] * nums[i], nums[i])
                local_min[i] = min(local_max[i - 1] * nums[i], nums[i])
            else:
                local_max[i] = max(local_max[i - 1] * nums[i], nums[i])
                local_min[i] = min(local_min[i - 1] * nums[i], nums[i])
            ans = max(ans, local_max[i])

        return ans


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [2, 3, -2, 4]
    assert s.maxProduct(nums) == 6

    # Example 2
    nums = [-2, 0, -1]
    assert s.maxProduct(nums) == 0

    # Example 3
    nums = [-2, 3, -4]
    assert s.maxProduct(nums) == 24

    print("All tests passed.")
