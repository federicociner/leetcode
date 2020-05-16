"""Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its
neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity sake, each node's value is the same as the node's index
(1-indexed). For example, the first node with val = 1, the second node with
val = 2, and so on. The graph is represented in the test case using an
adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite
graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the
copy of the given node as a reference to the cloned graph.

Example 1:

    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1) neighbors are 2nd node (val = 2) and 4th node (val =
    4).
    2nd node (val = 2) neighbors are 1st node (val = 1) and 3rd node (val =
    3).
    3rd node (val = 3) neighbors are 2nd node (val = 2) and 4th node (val =
    4).
    4th node (val = 4) neighbors are 1st node (val = 1) and 3rd node (val =
    3).

Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph
    consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.

Example 4:

    Input: adjList = [[2],[1]]
    Output: [[2],[1]]
Constraints:

    - 1 <= Node.val <= 100
    - Node.val is unique for each node.
    - Number of Nodes will not exceed 100.
    - There is no repeated edges and no self-loops in the graph.
    - The Graph is connected and all nodes can be visited starting from the
    given node.

"""
from typing import Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def __init__(self):
        self.graph = {}

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        # initial copy
        node_copy = Node(node.val, [])
        tmp = {node: node_copy}
        self.graph = tmp

        # run DFS recursively
        self.dfs(node, self.graph)

        return node_copy

    def dfs(self, node: "Node", graph: Dict["Node", "Node"]) -> "Node":
        for neighbor in node.neighbors:
            if neighbor not in graph:
                neighbor_copy = Node(neighbor.val, [])
                graph[neighbor] = neighbor_copy
                graph[node].neighbors.append(neighbor_copy)
                self.dfs(neighbor, graph)
            else:
                graph[node].neighbors.append(graph[neighbor])


if __name__ == "__main__":
    S = Solution()

    # Example 1
    n1 = Node(1, [])
    n2 = Node(2, [])
    n3 = Node(3, [])
    n4 = Node(4, [])
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    result = S.cloneGraph(n1)
    expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
    actual = []

    for k, v in S.graph.items():
        actual.append([n.val for n in v.neighbors])

    assert len(expected) == len(actual)
    assert expected == actual

    print("All tests passed.")
