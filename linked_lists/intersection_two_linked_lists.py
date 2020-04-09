"""Write a program to find the node at which the intersection of two singly
linked lists begins.

Example 1:

    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA
    = 2, skipB = 3

    Output: Reference of the node with value = 8

    Input Explanation: The intersected node's value is 8 (note that this must
    not be 0 if the two lists intersect). From the head of A, it reads as [4,1,
    8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes
    before the intersected node in A; There are 3 nodes before the intersected
    node in B.

Example 2:

    Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3,
    skipB = 1

    Output: Reference of the node with value = 2

    Input Explanation: The intersected node's value is 2 (note that this must
    not be 0 if the two lists intersect). From the head of A, it reads as [0,9,
    1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before
    the intersected node in A; There are 1 node before the intersected node in
    B.

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
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> ListNode:
        if not headA or not headB:
            return None

        a = headA
        b = headB

        while a and b and a != b:
            a = a.next
            b = b.next

            if a == b:
                return b

            if not a:
                a = headB

            if not b:
                b = headA

        return a


if __name__ == "__main__":
    # Example 1
    headA = ListNode(4)
    n1 = ListNode(1)
    n2 = ListNode(8)
    n3 = ListNode(4)
    n4 = ListNode(5)
    headA.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    headB = ListNode(5)
    a1 = ListNode(0)
    a2 = ListNode(1)
    headB.next = a1
    a1.next = a2
    a2.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    intersection = s.getIntersectionNode(headA, headB)
    assert intersection.val == 8

    print("All tests passed.")
