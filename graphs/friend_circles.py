"""There are N students in a class. Some of them are friends, while some are
not. Their friendship is transitive in nature. For example, if A is a direct
friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or
indirect friends.

Given a N*N matrix M representing the friend relationship between students in
the class. If M[i][j] = 1, then the ith and jth students are direct friends
with each other, otherwise not. And you have to output the total number of
friend circles among all the students.

Example 1:
    Input:
    [[1,1,0],
    [1,1,0],
    [0,0,1]]

    Output: 2

    Explanation:The 0th and 1st students are direct friends, so they are in a
    friend circle.
    The 2nd student himself is in a friend circle. So return 2.

Example 2:

    Input:
    [[1,1,0],
    [1,1,1],
    [0,1,1]]

    Output: 1

    Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
    students are direct friends, so the 0th and 2nd students are indirect
    friends. All of them are in the same friend circle, so return 1.

Note:
    N is in range [1,200].
    M[i][i] = 1 for all students.
    If M[i][j] = 1, then M[j][i] = 1.

"""
from typing import List


class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        n = len(M)
        visited = [False] * n
        count = 0

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                count += 1
                self.dfs(M, visited, node)

        return count

    def dfs(self, M: List[List[int]], visited: List[bool], u: int):
        n = len(M)

        for v in range(n):
            if M[u][v] == 1 and not visited[v]:
                visited[v] = True
                self.dfs(M, visited, v)


if __name__ == "__main__":
    S = Solution()

    # Example 1
    M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

    assert S.findCircleNum(M) == 2

    # Example 1
    M = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    assert S.findCircleNum(M) == 1

    print("All tests passed.")
