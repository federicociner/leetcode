"""Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

Example:

    Input: [1,1,2]
    Output:
    [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]

"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = []
        res = []

        self.backtrack(sorted(nums), visited, [], res)

        return res

    def backtrack(
        self,
        nums: List[int],
        visited: List[int],
        sub: List[int],
        res: List[List[int]],
    ):
        if len(sub) == len(nums):
            res.append(sub)
            return

        for i in range(len(nums)):
            if i not in visited:
                visited.append(i)
                self.backtrack(nums, visited, sub + [nums[i]], res)
                visited.remove(i)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.permuteUnique([1, 2, 2])
    print(actual)
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)
