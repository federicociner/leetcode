"""Given a collection of distinct integers, return all possible permutations.

Example:

    Input: [1,2,3]
    Output:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]

"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = []
        res = []

        self.backtrack(nums, visited, [], res)

        return res

    def backtrack(
        self,
        nums: List[int],
        visited: List[int],
        sub: List[int],
        res: List[List[int]],
    ):
        if len(sub) == len(nums) and sub not in res:
            res.append(sub)

        for i in range(len(nums)):
            if i not in visited:
                visited.append(i)
                self.backtrack(nums, visited, sub + [nums[i]], res)
                visited.remove(i)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.permute([1, 2, 3])
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)
