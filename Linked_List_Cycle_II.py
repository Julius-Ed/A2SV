class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):

        seen = set()

        curr = head

        while curr:
            if curr in seen:
                return curr

            else:
                seen.add(curr)

            curr = curr.next

        return None


Sol = Solution()


head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = head.next.next.next.next


print(Sol.detectCycle(head))
