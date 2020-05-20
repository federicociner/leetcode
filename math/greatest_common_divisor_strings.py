"""For strings S and T, we say "T divides S" if and only if S = T + ... + T
(T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:

    Input: str1 = "LEET", str2 = "CODE"

Output: ""

Note:

    - 1 <= str1.length <= 1000
    - 1 <= str2.length <= 1000
    - str1[i] and str2[i] are English uppercase letters.

"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ""
        else:
            if len(str1) < len(str2):
                str1, str2 = str2, str1

            if str1[: len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2) :], str2)
            else:
                return ""


if __name__ == "__main__":
    S = Solution()

    # Example 1
    str1 = "ABCABC"
    str2 = "ABC"
    assert S.gcdOfStrings(str1, str2) == "ABC"

    # Example 1
    str1 = "LEET"
    str2 = "CODE"
    assert S.gcdOfStrings(str1, str2) == ""

    print("All tests passed.")
