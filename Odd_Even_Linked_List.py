# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):

        if not head:
            return None

        even_dummy = ListNode("even")
        even_cursor = even_dummy
        odd_dummy = ListNode("odd")
        odd_cursor = odd_dummy

        odd = head
        even = head.next

        while even or odd:

            if even:
                even_cursor.next = even
                even_cursor = even_cursor.next

                if even:
                    even = even.next
                    #even = even.next.next
                    if even:
                        even = even.next
            else:
                even_cursor.next = None # test
            
            if odd:
                odd_cursor.next = odd
                odd_cursor = odd_cursor.next
                #odd_cursor.next = None # test
                if odd:
                    odd = odd.next
                    #odd = odd.next.next
                    if odd:
                        odd = odd.next
            else:
                odd_cursor.next = None
        
        odd_cursor.next = even_dummy.next

        return odd_dummy.next
        




    

Sol = Solution()



head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
# head.next.next.next.next.next = ListNode(4)
# head.next.next.next.next.next.next = ListNode(7)


Sol.oddEvenList(head)


