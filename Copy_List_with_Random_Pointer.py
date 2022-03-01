from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {None: None}

        current = head

        while current:
            copy = Node(current.val, None, None)
            oldToNew[current] = copy
            current = current.next

        current = head
        while current:

            next = oldToNew[current.next]
            rand = oldToNew[current.random]

            new = oldToNew[current]
            new.next = next
            new.random = rand
        

        return oldToNew[head]


