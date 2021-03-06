"""Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key.

The right subtree of a node contains only nodes with keys greater than the
node's key.

Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

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
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, node, lower, upper):
        if not node:
            return True

        val = node.val

        if val <= lower or val >= upper:
            return False

        if not self.dfs(node.right, val, upper):
            return False
        if not self.dfs(node.left, lower, val):
            return False

        return True


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
