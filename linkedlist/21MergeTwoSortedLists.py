# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        cur = dummy_head
        while l1 is not None or l2 is not None:
            if l1 is None:
                cur.next = l2
                l2 = l2.next
            elif l2 is None:
                cur.next = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
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
    l1.next = ListNode(3)
    l1.next.next = ListNode(6)
    l2 = ListNode(2)
    l2.next = ListNode(3)
    iterate_linked_list(solution.mergeTwoLists(l1,l2))
