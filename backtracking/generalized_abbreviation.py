"""Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

    Input: "word"
    Output:
    [
        "word",
        "1ord",
        "w1rd",
        "wo1d",
        "wor1",
        "2rd",
        "w2d",
        "wo2",
        "1o1d",
        "1or1",
        "w1r1",
        "1o2",
        "2r1",
        "3d",
        "w3",
        "4"
    ]

"""
from typing import List


class Solution:
    # Time complexity: O(n * 2^n)
    # Space complexity: O(n)
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []
        self.dfs(word, "", ans)

        return ans

    def dfs(self, word: str, sub: str, ans: List[str]) -> None:
        if not word:
            ans.append(sub)

        for i in range(1, len(word) + 1):
            if not sub or sub[-1].isalpha():
                self.dfs(word[i:], sub + str(i), ans)
            if not sub or sub[-1].isnumeric():
                self.dfs(word[i:], sub + word[:i], ans)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    word = "word"
    actual = s.generateAbbreviations(word)
    expected = [
        "word",
        "1ord",
        "w1rd",
        "wo1d",
        "wor1",
        "2rd",
        "w2d",
        "wo2",
        "1o1d",
        "1or1",
        "w1r1",
        "1o2",
        "2r1",
        "3d",
        "w3",
        "4",
    ]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
