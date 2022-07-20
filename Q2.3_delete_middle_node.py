def deleteMid(head):
    
    lst = []
    curr = head
    while curr is not None:
        lst.append(curr.data)
        curr = curr.next
    
    mid = len(lst) // 2     
    
    c = remove_at(head, mid)
    
    if len(lst) == 1:
        return 
    else:
        return c
        
        
def remove_at(head, index):
    count = 0
    curr = head
    
    while curr is not None:
        if count == index-1:
            curr.next = curr.next.next
        curr = curr.next
        count += 1
        
    return head