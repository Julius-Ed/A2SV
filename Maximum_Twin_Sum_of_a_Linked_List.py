
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head) -> int:

        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        cur = head
        for _ in range((n//2) - 1):
            cur = cur.next
        
        new_head = self.reverseList(cur.next)
        cur.next = new_head
    
        fast = head
        slow = head

        for _ in range(n//2):
            fast = fast.next
        
        twin_sum = 0
        while fast:

            if twin_sum < slow.val + fast.val:
                twin_sum = slow.val + fast.val
            
            fast = fast.next
            slow = slow.next
        
        return twin_sum



    def reverseList(self, head):
        
        prev = None
        current = head


        while current:

            temp_next = current.next

            current.next = prev
            prev = current
            current = temp_next

        return prev


Sol = Solution()


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)

print(Sol.pairSum(head))