"""Consider all the leaves of a binary tree. From left to right order, the
values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
8).

Two binary trees are considered leaf-similar if their leaf value sequence is
the same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.

Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200

"""


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
    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = self.dfs(root1)
        leaves2 = self.dfs(root2)

        return leaves1 == leaves2

    def dfs(self, node: TreeNode):
        if not node:
            return []

        if not node.left and not node.right:
            return [node.val]

        return self.dfs(node.left) + self.dfs(node.right)


if __name__ == "__main__":
    S = Solution()

    # Example 1
    root1 = TreeNode(3)
    n1 = TreeNode(5)
    n2 = TreeNode(1)
    n3 = TreeNode(6)
    n4 = TreeNode(2)
    n5 = TreeNode(9)
    n6 = TreeNode(8)
    n7 = TreeNode(7)
    n8 = TreeNode(4)
    root1.left = n1
    root1.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    n4.left = n7
    n4.right = n8

    root2 = TreeNode(3)
    n1 = TreeNode(5)
    n2 = TreeNode(1)
    n3 = TreeNode(6)
    n4 = TreeNode(2)
    n5 = TreeNode(9)
    n6 = TreeNode(8)
    n7 = TreeNode(7)
    n8 = TreeNode(4)
    root2.left = n1
    root2.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    n4.left = n7
    n4.right = n8

    assert S.leafSimilar(root1, root2) is True

    print("All tests passed.")
