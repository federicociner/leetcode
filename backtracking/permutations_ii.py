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
    # Time complexity: O(n * n!)
    # Space complexity: O(n!)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        res = []

        self.backtrack(sorted(nums), visited, [], res)

        return res

    def backtrack(
        self,
        nums: List[int],
        visited: List[int],
        sub: List[int],
        res: List[List[int]],
    ) -> None:
        if len(sub) == len(nums):
            res.append(sub)

        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                visited[i] = True
                self.backtrack(nums, visited, sub + [nums[i]], res)
                visited[i] = False


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.permuteUnique([1, 1, 2])
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    # Example 2
    actual = s.permuteUnique([1, 3, 3])
    expected = [[1, 3, 3], [3, 1, 3], [3, 3, 1]]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
