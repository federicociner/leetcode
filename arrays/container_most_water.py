"""Given n non-negative integers a1, a2, ..., an, where each represents a
point at coordinate (i, ai), n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water = float("-inf")

        while i < j:
            width = j - i
            water = max(water, width * min(height[i], height[j]))

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return water


if __name__ == "__main__":
    s = Solution()

    # Example 1
    x = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(x) == 49

    # Example 2
    x = [4, 9, 8, 2, 3, 7, 6, 4, 5]
    assert s.maxArea(x) == 35

    print("All tests passed.")
