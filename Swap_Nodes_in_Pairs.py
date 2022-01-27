# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def swapPairs(self, head):
        
        prev = None
        cursor = head

        while cursor:

            if not cursor.next:
                return head
    
            temp_next = cursor.next.next
    
            new_head, new_tail = self.swapPair(cursor)

            if prev:
                prev.next = new_head
            else:
                head = new_head
            
            if cursor.next.next:
                new_tail.next = temp_next

            prev = new_tail
            cursor = prev.next

        
        return head



    def swapPair(self, prev):

        curr = prev.next

        temp_next = curr
        curr.next = prev
        prev.next = temp_next

        new_head = temp_next
        new_tail = prev

        return new_head, new_tail
    



Sol = Solution()



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)


print(Sol.swapPairs(head))




