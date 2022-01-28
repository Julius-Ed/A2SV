# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head, k: int):
        if head is None:
            return [None] * k

        result = []

        length = self.get_length(head)

        moves = length // k
        remainder = length % k

        curr = head

        while curr:

            if remainder > 0:
                actual_moves = moves + 1
                remainder -= 1
            else:
                actual_moves = moves

            result.append(curr)
            for _ in range(actual_moves):
                prev = curr
                curr = curr.next
            prev.next = None

        while len(result) < k:
            result.append(None)

        return result

    def get_length(self, head):
        n, curr = 0, head
        while curr:
            curr = curr.next
            n += 1

        return n


Sol = Solution()


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next.next.next = ListNode(9)
# head.next.next.next.next.next.next.next.next.next = ListNode(10)
# head.next.next.next.next.next.next.next.next.next.next = ListNode(11)

head = None


result_list = Sol.splitListToParts(head, 3)


for head in result_list:

    curr = head

    print("new head:")
    while curr:
        print(curr.val)
        curr = curr.next
