class ListNode:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next


def has_cycle(head):

    if not head:
        return 0

    fast = head
    slow = head

    while slow:

        if fast == slow:
            return 1
        
        fast = fast.next.next
        slow = slow.next
        
    return 0

def has_cycle(head):
    
    if not head:
        return 0

    storer = set()
    
    cur = head
    
    while cur:
        if cur in storer:
            return 1
        else:
            storer.add(cur)
            cur = cur.next
    return 0