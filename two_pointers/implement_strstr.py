"""Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().

"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        L = len(needle)
        n = len(haystack)

        if L == 0:
            return 0

        pn = 0

        while pn < n - L + 1:
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            curr = 0
            pL = 0

            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr += 1

            if curr == L:
                return pn - L

            pn = (pn - curr) + 1

        return -1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    haystack = "hello"
    needle = "ll"
    assert s.strStr(haystack, needle) == 2

    # Example 2
    haystack = "aaaaa"
    needle = "bba"
    assert s.strStr(haystack, needle) == -1

    print("All tests passed.")
