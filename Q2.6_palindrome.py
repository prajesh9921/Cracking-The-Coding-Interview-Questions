class Solution:
    def isPalindrome(self, head):
        lst = []
        
        temp = head
        while temp is not None:
            lst.append(temp.data)
            temp = temp.next
        
        lst_rev = lst[::-1]
        
        if lst == lst_rev:
            return True
        else:
            return False
