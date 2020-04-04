"""Given a collection of integers that might contain duplicates, nums, return
all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

    Input: [1,2,2]

    Output:
    [
        [2],
        [1],
        [1,2,2],
        [2,2],
        [1,2],
        []
    ]

"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []
        self.dfs(sorted(nums), 0, [], res)

        return res

    def dfs(
        self, nums: List[int], index: int, sub: List[int], res: List[List[int]]
    ):
        if sub not in res:
            res.append(sub)

        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, sub + [nums[i]], res)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    expected = [[2], [1], [1, 2, 2], [2, 2], [1, 2], []]
    actual = s.subsetsWithDup([1, 2, 2])

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    # Example 2
    expected = [
        [],
        [1],
        [1, 4],
        [1, 4, 4],
        [1, 4, 4, 4],
        [1, 4, 4, 4, 4],
        [4],
        [4, 4],
        [4, 4, 4],
        [4, 4, 4, 4],
    ]
    actual = s.subsetsWithDup([4, 4, 4, 1, 4])

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
