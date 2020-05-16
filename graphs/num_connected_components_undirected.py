"""Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
edge is a pair of nodes), write a function to find the number of connected
components in an undirected graph.

Example 1:

    Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

        0          3
        |          |
        1 --- 2    4

    Output: 2

Example 2:

    Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

        0           4
        |           |
        1 --- 2 --- 3

    Output:  1

Note:

    You can assume that no duplicate edges will appear in edges. Since all
    edges are undirected, [0, 1] is the same as [1, 0] and thus will not
    appear together in edges.

"""
from typing import Dict
from typing import List


class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        count = 0

        graph = {node: [] for node in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            if not visited[node]:
                self.dfs(graph, visited, node)
                count += 1

        return count

    def dfs(
        self, graph: Dict[int, List[int]], visited: List[bool], node: int
    ) -> None:
        if visited[node]:
            return

        visited[node] = True

        for u in graph[node]:
            self.dfs(graph, visited, u)


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]

    assert S.countComponents(n, edges) == 2

    # Example 1
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

    assert S.countComponents(n, edges) == 1

    print("All tests passed.")
