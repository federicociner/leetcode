"""Given an array of integers nums and a positive integer k, find whether it's
possible to divide this array into k non-empty subsets whose sums are all
equal.

Example 1:

    Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
    Output: True
    Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
    (2,3) with equal sums.

Note:

    1 <= k <= len(nums) <= 16.
    0 < nums[i] < 10000.

"""
from typing import List


class Solution:
    # Time complexity: O(k * 2^n)
    # Space complexity: O(k * 2^n)
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)

        if remainder != 0:
            return False

        visited = [False] * len(nums)

        return self.backtrack(nums, visited, target, k, 0, 0)

    def backtrack(
        self,
        nums: List[int],
        visited: List[bool],
        target: int,
        k: int,
        index: int,
        val: int,
    ) -> bool:
        if k == 0:
            return True

        if val == target:
            return self.backtrack(nums, visited, target, k - 1, 0, 0)

        for i in range(index, len(nums)):
            if val + nums[i] <= target and not visited[i]:
                visited[i] = True
                if self.backtrack(
                    nums, visited, target, k, i + 1, val + nums[i]
                ):
                    return True
                visited[i] = False

        return False


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    assert s.canPartitionKSubsets(nums, k) is True

    print("All tests passed.")
