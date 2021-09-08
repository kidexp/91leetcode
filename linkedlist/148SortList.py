# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_list(l1, l2):
    cur = dummy_head = ListNode()
    while l1 or l2:
        if not l1:
            cur.next = l2
            l2 = l2.next
        elif not l2:
            cur.next = l1
            l1 = l1.next
        elif l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    return dummy_head.next


def divide_list(head):
    if not head:
        return None, None
    if not head.next:
        return head, None
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    next_head = slow.next
    slow.next = None
    return head, next_head


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        l1, l2 = divide_list(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return merge_list(l1, l2)


def iterate_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print("")
    print("===============")


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(4)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(1)
    iterate_linked_list(solution.sortList(l1))
    l1 = ListNode(4)
    l1.next = ListNode(3)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(1)
    iterate_linked_list(solution.sortList(l1))
    l1 = ListNode(4)
    l1.next = ListNode(1)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(2)
    iterate_linked_list(solution.sortList(l1))
    l1 = ListNode(4)
    l1.next = ListNode(5)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(1)
    iterate_linked_list(solution.sortList(l1))
