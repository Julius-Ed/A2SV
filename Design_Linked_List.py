
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
        
        # if not prev and curr:
        #     self.addAtHead(val)
        
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
            #curr.next = None
            prev.next = curr.next
        
        if curr and (not prev and curr.next):
            self.head = self.head.next
        
        if curr and (prev and not curr.next):
            prev.next = None


    def traverse(self):

        curr = self.head
        print("\n")
        while curr:
            print(curr.val)
            curr = curr.next
        print("\n")


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



Sol = MyLinkedList()
Sol.traverse()
Sol.addAtHead(1)
Sol.traverse()
Sol.addAtTail(3)
Sol.traverse()
Sol.addAtIndex(1, 2)
Sol.traverse()
Sol.get(1)
Sol.traverse()
Sol.deleteAtIndex(1)
Sol.traverse()
Sol.get(1)
Sol.traverse()
Sol.get(3)
Sol.traverse()
Sol.deleteAtIndex(3)
Sol.traverse()
Sol.deleteAtIndex(0)
Sol.traverse()
Sol.get(0)
Sol.traverse()
Sol.deleteAtIndex(0)
Sol.traverse()
print(Sol.get(0))
Sol.traverse()
