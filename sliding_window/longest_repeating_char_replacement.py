"""Given a string s that consists of only uppercase English letters, you can
perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to
any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you
can get after performing the above operations.

Note:
    Both the string's length and k will not exceed 104.

Example 1:

    Input:
    s = "ABAB", k = 2

    Output:
    4

    Explanation:
    Replace the two 'A's with two 'B's or vice versa.

Example 2:

    Input:
    s = "AABABBA", k = 1

    Output:
    4

    Explanation:
    Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.

"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        occurences = {}
        left = 0
        max_len = 0
        max_repeat_count = 0

        for right in range(len(s)):
            curr = s[right]

            if curr not in occurences:
                occurences[curr] = 1
            else:
                occurences[curr] += 1

            max_repeat_count = max(max_repeat_count, occurences[curr])

            if (right - left + 1 - max_repeat_count) > k:
                left_char = s[left]
                occurences[left_char] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    S = Solution()

    # Example 1
    s = "ABAB"
    assert S.characterReplacement(s, 2) == 4

    # Example 2
    s = "AABABBA"
    assert S.characterReplacement(s, 1) == 4

    print("All tests passed.")
