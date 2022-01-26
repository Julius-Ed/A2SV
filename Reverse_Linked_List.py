class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        
        prev = None
        current = head


        while current:

            temp_next = current.next

            current.next = prev
            prev = current
            current = temp_next

        return prev



Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)


Sol = Solution()
new_head = Sol.reverseList(Head)

while new_head:
    print(new_head.val)
    new_head = new_head.next