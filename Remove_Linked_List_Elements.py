

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):

        if not head:
            return 
        
        prev = None
        curr = head

        while curr:

            if curr.val == val:
                
                if prev is None:
                    head = head.next

                    prev = None
                    curr = head

                
                elif curr.next is None:
                    prev.next = None
                    return head

                else:
                    prev.next= curr.next
                    curr = curr.next

    
            else:
                prev = curr
                curr = curr.next
        
        return head
    
    def traverse(self, head):
        curr = head

        while curr:
            print(curr.val)
            curr = curr.next


Sol = Solution()


head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(6)
# head.next.next.next = ListNode(6)
# head.next.next.next.next = ListNode(4)
# head.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next = ListNode(6)

# head = ListNode(6)
# head.next = ListNode(6)
# head.next.next = ListNode(6)
# head.next.next.next = ListNode(6)


head = Sol.removeElements(head, 1)
Sol.traverse(head)