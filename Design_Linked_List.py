
class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    # Get the value of the indexth node in the linked list. If the index is invalid, return -1
    def get(self, index: int) -> int:
        curr = self.head

        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1

        if curr and i == index:
            return curr.val
        else:
            return -1

    # Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node

    # Append a node of value val as the last element of the linked list.
    def addAtTail(self, val: int) -> None:
        curr = self.head

        if not curr:
            self.addAtHead(val)
            return

        while curr.next:
            curr = curr.next

        curr.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)

        prev = None
        curr = self.head

        i = 0
        while curr and i < index:
            prev = curr
            curr = curr.next
            i += 1

        if curr and prev:
            prev.next = ListNode(val, curr)

        if not curr and prev:
            self.addAtTail(val)

    # Delete the indexth node in the linked list, if the index is valid.
    def deleteAtIndex(self, index: int) -> None:
        if self.head and not self.head.next and index == 0:
            self.head = None
            return

        prev = None
        curr = self.head

        i = 0
        while curr and i < index:
            prev = curr
            curr = curr.next
            i += 1

        if curr and (prev and curr.next):
            prev.next = curr.next

        if curr and (not prev and curr.next):
            self.head = self.head.next

        if curr and (prev and not curr.next):
            prev.next = None