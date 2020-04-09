"""Write a function to delete a node (except the tail) in a singly linked
list, given only access to that node.

Example 1:

    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list
    should become 4 -> 1 -> 9 after calling your function.

Example 2:

    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked list
    should become 4 -> 5 -> 9 after calling your function.

Note:

    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of
    the linked list.
    Do not return anything from your function.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    # Example 1
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n4 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    s.deleteNode(n2)

    e1 = ListNode(4)
    e2 = ListNode(1)
    e3 = ListNode(9)
    e1.next = e2
    e2.next = e3

    temp1 = n1
    temp2 = e1

    while temp1 is not None:
        assert temp1.val == temp2.val
        temp1 = temp1.next
        temp2 = temp2.next

    print("All tests passed.")
