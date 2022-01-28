# Definition for singly-linked list.
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head):

        self.head = head

        cur = head
        self.length = 0

        while cur:
            self.length += 1
            cur = cur.next

    def getRandom(self) -> int:

        if not self.head:
            return

        i = random.randrange(0, self.length)
        curr = self.head

        steps = 0
        while steps < i:
            curr = curr.next
            steps += 1

        return curr.val


head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)

Sol = Solution(head_node)
print(Sol.getRandom())
