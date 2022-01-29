

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head):
        
        sum_values = {}
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        sum = 0

        while current:
            if current.val == 0: 
                prev.next = current.next
                prev = dummy
                current = prev.next
                sum_values = {}
                sum = 0
                continue

            sum += current.val

            if sum == 0:
                dummy.next = current.next
                current = current.next
                sum = 0
                continue

            if sum in sum_values:
                prev = sum_values[sum]
                prev.next = current.next
                sum = 0

                sum_values = {}

                prev = dummy
                current = prev.next
            
            else:
                sum_values[sum] = current

                prev = current
                current = current.next
        
        return dummy.next


    



Sol = Solution()

head = ListNode(0)
head.next = ListNode(-3)
head.next.next = ListNode(-4)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(-2)
head.next.next.next.next.next.next = ListNode(-5)

head = Sol.removeZeroSumSublists(head)

print(" ")
while head:
    print(head.val)
    head = head.next