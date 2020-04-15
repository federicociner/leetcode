"""Given a set of candidate numbers (candidates) (without duplicates) and a
target number (target), find all unique combinations in candidates where the
candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of
times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

    Input: candidates = [2,3,6,7], target = 7
    A solution set is:
    [
        [7],
        [2,2,3]
    ]

Example 2:

    Input: candidates = [2,3,5], target = 8
    A solution set is:
    [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]

"""
from typing import List


class Solution:
    # Time complexity: O(k * 2^n)
    # Space complexity: O(k * 2^n)
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        ans = []
        self.backtrack(candidates, target, 0, [], ans)

        return ans

    def backtrack(
        self,
        nums: List[int],
        target: int,
        index: int,
        sub: List[int],
        ans: List[List[int]],
    ) -> None:
        if target < 0:
            return

        if target == 0:
            ans.append(sub)

            return

        for i in range(index, len(nums)):
            self.backtrack(nums, target - nums[i], i, sub + [nums[i]], ans)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.combinationSum([2, 3, 6, 7], 7)
    expected = [[7], [2, 2, 3]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    # Example 2
    actual = s.combinationSum([2, 3, 5], 8)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
