"""Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

    Input: candidates = [10,1,2,7,6,1,5], target = 8
    A solution set is:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]

Example 2:

    Input: candidates = [2,5,2,1,2], target = 5
    A solution set is:
    [
        [1,2,2],
        [5]
    ]

"""
from typing import List


class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        res = []
        self.backtrack(sorted(candidates), target, 0, [], res)

        return res

    def backtrack(
        self,
        nums: List[int],
        target: int,
        index: int,
        sub: List[int],
        res: List[List[int]],
    ):
        if target < 0:
            return

        if target == 0:
            res.append(sub)

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break

            self.backtrack(nums, target - nums[i], i + 1, sub + [nums[i]], res)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    expected = [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    # Example 2
    actual = s.combinationSum2([2, 5, 2, 1, 2], 5)
    expected = [[1, 2, 2], [5]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)