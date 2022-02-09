def findMergeNode(head1, head2):
    
    seen = set()
    seenCurrent2 = set()
    
    current1 = head1
    current2 = head2
    
    
    # what if we have a cycle in the LinkedList?
    while current1:
        if current1 not in seen:
            seen.add(current1)
        else:
            return "detected cycle in current1 path"
        current1 = current1.next

    
    while current2:
        if current2 in seen:
            # detected merge point
            return current2.data
    
        if current2 not in seenCurrent2:
            seenCurrent2.add(current2)
        else:
            return "detected cycle in current2 path"
        
        current2 = current2.next

    # return None if the two lists don't merge
    return None