from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB
        finish = False
        while l1 != l2:
            if l1.next is None and l2.next is None:
                if finish:
                    return None
            if l1.next is None:
                l1 = headB
                finish = True
            else:
                l1 = l1.next
            if l2.next is None:
                l2 = headA
            else:
                l2 = l2.next
        return l1


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(5)
    l2 = ListNode(3)
    l2.next = ListNode(4)
    l2.next.next = l1.next.next
    l2.next.next.next = l1.next.next.next
    print(solution.getIntersectionNode(l1, l2).val)
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(4)
    l2 = ListNode(3)
    l2.next = ListNode(4)
    l2.next.next = ListNode(4)
    print(solution.getIntersectionNode(l1, l2))
