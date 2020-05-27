"""Given the root of a binary tree, find the maximum average value of any
subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The
average value of a tree is the sum of its values, divided by the number of
nodes.)

Example 1:

    Input: [5, 6, 1]
    Output: 6.00000
    Explanation:
    For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
    For the node with value = 6 we have an average of 6 / 1 = 6.
    For the node with value = 1 we have an average of 1 / 1 = 1.
    So the answer is 6 which is the maximum.

Note:

    - The number of nodes in the tree is between 1 and 5000.
    - Each node will have a value between 0 and 100000.
    - Answers will be accepted as correct if they are within 10^-5 of the
    correct answer.

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
    def __init__(self):
        self.ans = float("-inf")

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0

        self.dfs(root)

        return self.ans

    def dfs(self, node: TreeNode):
        if not node:
            return [0, 0]

        left_sum, left_num = self.dfs(node.left)
        right_sum, right_num = self.dfs(node.right)

        curr_sum = node.val + left_sum + right_sum
        curr_num = 1 + left_num + right_num

        self.ans = max(self.ans, curr_sum / curr_num)

        return [curr_sum, curr_num]


if __name__ == "__main__":
    S = Solution()

    # Example 1
    root = TreeNode(5)
    n1 = TreeNode(6)
    n2 = TreeNode(1)
    root.left = n1
    root.right = n2

    assert S.maximumAverageSubtree(root) == 6.0

    print("All tests passed.")
