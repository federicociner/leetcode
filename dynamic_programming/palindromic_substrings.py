"""Given a string, your task is to count how many palindromic substrings in
this string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.

Example 1:

    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""


class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        max_count = 0

        for i in range(len(s)):
            max_count += self.expand(s, i, i)
            max_count += self.expand(s, i, i + 1)

        return max_count

    def expand(self, s: str, left: int, right: int) -> int:
        count = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        return count


if __name__ == "__main__":
    S = Solution()

    # Example 1
    s = "abc"
    assert S.countSubstrings(s) == 3

    # Example 2
    s = "aaa"
    assert S.countSubstrings(s) == 6

    print("All tests passed.")
