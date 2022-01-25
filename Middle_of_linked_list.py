# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        
        current = head
        n = 0

        while current:
            n += 1
            current = current.next
        
        if n % 2 == 0:
            median = (n // 2) + 1
        else:
            median = (n + 1) // 2
        
        current = head

        while median > 1:

            current = current.next
            median -= 1

        return current
