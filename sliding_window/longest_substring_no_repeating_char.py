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


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(k), where k is the size of the set
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 0
        ans = 0
        seen = set()

        while left < len(s) and right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:
                seen.remove(s[left])
                left += 1

        return ans


if __name__ == "__main__":
    S = Solution()

    # Example 1
    s = "abcabcbb"
    assert S.lengthOfLongestSubstring(s) == 3

    # Example 2
    s = "bbbbb"
    assert S.lengthOfLongestSubstring(s) == 1

    # Example 3
    s = "pwwkew"
    assert S.lengthOfLongestSubstring(s) == 3

    print("All tests passed.")
