# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):

        if not lists or len(lists) == 0:
            return
        
        while len(lists) > 1:
            lists.append(self.merge_two_linked_lists(lists.pop(), lists.pop()))
        
        return lists[0]
        



    def merge_two_linked_lists(self, list_0, list_1):

        head = ListNode("dummy_head")
        tail = head

        curr_0 = list_0
        curr_1 = list_1

        while curr_0 and curr_1:

            if curr_0.val < curr_1.val:
                tail.next = curr_0
                curr_0 = curr_0.next
            else:
                tail.next = curr_1
                curr_1 = curr_1.next
                
            tail = tail.next

        if curr_0:
            tail.next = curr_0
        
        if curr_1:
            tail.next = curr_1
        
        return head.next



head_0 = ListNode(1)
head_0.next = ListNode(4)
head_0.next.next = ListNode(5)

head_1 = ListNode(1)
head_1.next = ListNode(3)
head_1.next.next = ListNode(4)

head_2 = ListNode(2)
head_2.next = ListNode(6)


Sol = Solution()

#final_head = Sol.mergeKLists([head_0, head_1, head_2])
print(Sol.mergeKLists([[]]))
# print(Sol.merge_two_linked_lists(head_0, head_1))


# while final_head:
#     print(final_head.val)
#     final_head = final_head.next