"""Given a singly linked list, group all odd nodes together followed by the
even nodes. Please note here we are talking about the node number and not the
value in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example 1:

    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

Example 2:

    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL

Constraints:

    - The relative order inside both the even and odd groups should remain as
    it was in the input.
    - The first node is considered odd, the second node even and so on ...
    - The length of the linked list is between [0, 10^4].

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


if __name__ == "__main__":
    # Example
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    expected = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(5)
    n3 = ListNode(2)
    n4 = ListNode(4)
    expected.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    actual = s.oddEvenList(head)
    temp1 = actual
    temp2 = expected

    while temp1 is not None:
        assert temp1.val == temp2.val
        temp1 = temp1.next
        temp2 = temp2.next

    print("All tests passed.")
