"""Given n nodes labeled from 0 to n-1 and a list of undirected edges (each
edge is a pair of nodes), write a function to check whether these edges make
up a valid tree.

Example 1:

    Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
    Output: true

Example 2:

    Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    Output: false

Note: you can assume that no duplicate edges will appear in edges. Since all
edges are undirected, [0,1] is the same as [1,0] and thus will not appear
together in edges.

"""
from typing import Dict
from typing import List


class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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

        if count == 1 and len(edges) < n:
            return True

        return False

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
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

    assert S.validTree(n, edges) is True

    # Example 1
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

    assert S.validTree(n, edges) is False

    print("All tests passed.")
