


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head):
        
        stack = []
        result = []
        idx_trac = 0

        cur = head

        while cur:
            result.append(0)

            while stack and cur.val > stack[-1][1]:
                idx, val = stack.pop()
                result[idx] = cur.val
            
            stack.append((idx_trac, cur.val))
            cur = cur.next
            idx_trac += 1

        return result

            


Sol = Solution()


head = ListNode(1)
head.next = ListNode(7)
head.next.next = ListNode(5)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(9)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next = ListNode(1)



print(Sol.nextLargerNodes(head))

