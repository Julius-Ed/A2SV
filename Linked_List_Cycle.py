# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        
        current = head
        seen = set()

        while current:
    
            if current in seen:
                return False
    
            seen.add(current)
            current = current.next
    
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

Sol = Solution()
print(Sol.hasCycle(head))


