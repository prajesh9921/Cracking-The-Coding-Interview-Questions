def detectLoop(head):
        
        dict = set()
        
        temp = head
        while temp is not None:
            
            if (temp in dict):
                return True
                
            dict.add(temp)
            temp = temp.next
            
        return False


# Using Floyd's Cycle finding Alogirithm

def detectLoop(head):

    slow_p = head
    fast_p = head
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return True
    return False


