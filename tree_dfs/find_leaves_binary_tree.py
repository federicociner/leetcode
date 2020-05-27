"""Given a binary tree, collect a tree's nodes as if you were doing this:
Collect and remove all leaves, repeat until the tree is empty.

Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2

2. Now removing the leaf [2] would result in this tree:

          1

3. Now removing the leaf [1] would result in the empty tree:

          []

"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, level=0):
        ret = "\t" * level + f"TreeNode: {repr(self.val)}" + "\n"

        if self.left:
            ret += self.left.__str__(level + 1)

        if self.right:
            ret += self.right.__str__(level + 1)

        return ret

    def __repr__(self):
        return "<tree node representation>"


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        leaves = []
        self.dfs(root, leaves)

        return leaves

    def dfs(self, node: TreeNode, leaves: List[List[int]]) -> None:
        if not node:
            return -1

        depth = 1 + (
            max(self.dfs(node.left, leaves), self.dfs(node.right, leaves))
        )

        if len(leaves) == depth:
            leaves.append([])

        leaves[depth].append(node.val)

        return depth


if __name__ == "__main__":
    S = Solution()

    # Example 1
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    n4 = TreeNode(5)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4

    assert S.findLeaves(root) == [[4, 5, 3], [2], [1]]

    print("All tests passed.")
