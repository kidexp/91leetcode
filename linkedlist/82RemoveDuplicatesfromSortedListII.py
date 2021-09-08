from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = dummy_head = ListNode()
        dummy_head.next = head
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return dummy_head.next


def iterate_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print("")
    print("===============")


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(2)
    iterate_linked_list(solution.deleteDuplicates(l1))
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(3)
    l1.next.next.next.next.next = ListNode(6)
    iterate_linked_list(solution.deleteDuplicates(l1))
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next.next = ListNode(5)
    iterate_linked_list(solution.deleteDuplicates(l1))
