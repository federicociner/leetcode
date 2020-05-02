"""You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version. You should
minimize the number of calls to the API.

Example:

    Given n = 5, and version = 4 is the first bad version.

    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true

    Then 4 is the first bad version.
"""


def isBadVersion(version: int, bad_version: int = 4) -> bool:
    return version == bad_version


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left < right:
            mid = left + ((right - left) // 2)

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    s = Solution()

    # Example 1
    n = 5
    assert s.firstBadVersion(n) == 4

    print("All tests passed.")
