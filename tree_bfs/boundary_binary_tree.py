"""Given a binary tree, return the values of its boundary in anti-clockwise
direction starting from root. Boundary includes left boundary, leaves, and
right boundary in order without duplicate nodes.  (The values of the nodes may
still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right
boundary is defined as the path from root to the right-most node. If the root
doesn't have left subtree or right subtree, then the root itself is left
boundary or right boundary. Note this definition only applies to the input
binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always
firstly travel to the left subtree if exists. If not, travel to the right
subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right
exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you
should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].


Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to
definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,
10,6,3].

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
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # Initialise boundary array
        boundary = []

        if not self.is_leaf(root):
            boundary.append(root.val)

        # Get left boundary
        nextNode = root.left
        while nextNode:
            if not self.is_leaf(nextNode):
                boundary.append(nextNode.val)
            if nextNode.left:
                nextNode = nextNode.left
            else:
                nextNode = nextNode.right

        # Get leaves
        self.find_leaves(root, boundary)

        # Get right boundary
        stack = []
        nextNode = root.right
        while nextNode:
            if not self.is_leaf(nextNode):
                stack.append(nextNode.val)
            if nextNode.right:
                nextNode = nextNode.right
            else:
                nextNode = nextNode.left

        while stack:
            boundary.append(stack.pop())

        return boundary

    def find_leaves(self, node: TreeNode, boundary: List[int]) -> None:
        if self.is_leaf(node):
            boundary.append(node.val)
        else:
            if node.left:
                self.find_leaves(node.left, boundary)
            if node.right:
                self.find_leaves(node.right, boundary)

    def is_leaf(self, node: TreeNode) -> bool:
        return node.left is None and node.right is None


if __name__ == "__main__":
    S = Solution()

    # Example 1
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    root.right = n1
    n1.left = n2
    n1.right = n3

    assert S.boundaryOfBinaryTree(root) == [1, 3, 4, 2]

    # Example 2
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)
    n10 = TreeNode(10)
    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n7
    n5.right = n8
    n3.left = n6
    n6.left = n9
    n6.right = n10

    assert S.boundaryOfBinaryTree(root) == [1, 2, 4, 7, 8, 9, 10, 6, 3]

    print("All tests passed.")
