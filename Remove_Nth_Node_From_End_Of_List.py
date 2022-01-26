class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):

        if head.next is None:
            pass

        fast = head
        slow = head
        prev = None

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next
    
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)        

Sol = Solution()
head = Sol.removeNthFromEnd(head)


while head:
    print(head.val)
    head = head.next