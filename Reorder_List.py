
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reorderList(self, head) -> None:

        if head is None or (head and head.next is None):
            return
        # elif head.next is None:
        #     return

        prev_slow = None
        slow = head
        fast = head

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        right = break_point = self.reverseList(slow)
        prev_slow.next = right

        left = head

        new_start = ListNode("new_head")
        tail = new_start

        while left != break_point:
            tail.next = left
            tail = tail.next 
            left = left.next

            tail.next = right
            tail = tail.next 
            right = right.next

        head = new_start


    def reverseList(self, head):
        
        prev = None
        current = head


        while current:

            temp_next = current.next

            current.next = prev
            prev = current
            current = temp_next

        return prev



    def reorderList1(self, head) -> None:

        if head is None:
            return
        
        left = head
        right_prev = None
        right = head

        while right.next:
            right_prev = right
            right = right.next
        
        while left != right and left.next != right:

            temp = left.next
            left.next = right
            right_prev.next = None
            right.next = temp

            left = temp

            while right.next:
                right_prev = right
                right = right.nextr
            
        

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

