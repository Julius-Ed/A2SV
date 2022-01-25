# Definition for singly-linked list.
from ctypes import pointer
from sympy import Li


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1, list2):
        
        head  = ListNode(0)    
        pointer = head 
        
        while list1 and list2:
    
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next   
         
            pointer = pointer.next

        if list1:
            pointer.next = list1
        
        elif list2:
            pointer.next = list2


        return head.next




head_0 = ListNode(1)
head_0.next = ListNode(2)
head_0.next.next = ListNode(4)

head_1 = ListNode(1)
head_1.next = ListNode(3)
head_1.next.next = ListNode(4)


Sol = Solution()
Sol.mergeTwoLists(head_0, head_1)

"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""