# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        current = ListNode("Dummy")
        new_head = current
        carry = 0

        while l1 or l2 or carry != 0:
            
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next

            
        
            new_value = carry % 10

            current.next = ListNode(new_value)
            current = current.next

            print(new_value)

            carry = carry // 10
        
        return new_head.next

l1 = ListNode(1)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(4)

# l1 = ListNode(9)
# l1.next = ListNode(9)
# l1.next.next = ListNode(9)

# l2 = ListNode(9)
# l2.next = ListNode(9)
# l2.next.next = ListNode(9)


Sol = Solution()
Sol.addTwoNumbers(l1, l2)