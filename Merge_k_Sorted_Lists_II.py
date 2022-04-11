# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:

            headOne, headTwo = lists.pop(), lists.pop()
            lists.append(self.merge(headOne, headTwo))

        return lists[0]

    def merge(self, headOne, headTwo):

        dummy = ListNode(0)

        currOne, currTwo, prev = headOne, headTwo, dummy

        while currOne and currTwo:
            if currOne.val <= currTwo.val:
                prev.next = currOne
                currOne = currOne.next

            else:
                prev.next = currTwo
                currTwo = currTwo.next

            prev = prev.next

        if currOne:
            prev.next = currOne
        elif currTwo:
            prev.next = currTwo

        return dummy.next


head_0 = ListNode(1)
head_0.next = ListNode(4)
head_0.next.next = ListNode(5)

head_1 = ListNode(1)
head_1.next = ListNode(3)
head_1.next.next = ListNode(4)

head_2 = ListNode(2)
head_2.next = ListNode(6)


Sol = Solution()

mergedHead = Sol.mergeKLists([head_0, head_1, head_2])
current = mergedHead
while current:
    print(current.val)
    current = current.next
