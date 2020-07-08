"""Given a string, find the length of the longest substring without repeating
characters.

Example 1:

    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

    Note that the answer must be a substring, "pwke" is a subsequence and not
    a substring.

"""
from typing import List
from collections import deque


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n * k == 0:
            return []

        if k == 1:
            return nums

        # init deque and output
        queue = deque()
        max_index = 0

        for i in range(k):
            self.clean_deque(nums, queue, k, i)
            queue.append(i)

            if nums[i] > nums[max_index]:
                max_index = i

        output = [nums[max_index]]

        # build output
        for i in range(k, n):
            self.clean_deque(nums, queue, k, i)
            queue.append(i)
            output.append(nums[queue[0]])

        return output

    def clean_deque(self, nums, queue, k, i):
        # remove indexes of elements not in sliding window
        if queue and queue[0] == i - k:
            queue.popleft()

        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()


class SolutionBruteForce:
    # Time complexity: O(n * k)
    # Space complexity: O(n - k + 1)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            ans.append(max(nums[i : i + k]))

        return ans


if __name__ == "__main__":
    S = Solution()

    # Example 1
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert S.maxSlidingWindow(nums, 3) == [3, 3, 5, 5, 6, 7]
    print("All tests passed.")
