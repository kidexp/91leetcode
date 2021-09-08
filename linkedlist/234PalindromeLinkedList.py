from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        # reverse l2
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        l2 = prev
        # compare
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next
        return True


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(1)
    print(solution.isPalindrome(l1))
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(1)
    print(solution.isPalindrome(l1))
    l1 = ListNode(1)
    l1.next = ListNode(2)
    print(solution.isPalindrome(l1))
