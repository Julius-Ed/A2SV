# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        
        
        if not head:
            return None
        
        if not head.next:
            return head
    
        current = head

        new_start = ListNode("0")
        new_head = new_start


        while current:

            while current.next and current.val == current.next.val:
                current = current.next

            new_start.next = current
            new_start = new_start.next

            current = current.next

        return new_head.next
            