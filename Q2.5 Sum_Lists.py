class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        
        first_num = ""
        second_num = ""
        
        ## convert first linked list into string
        temp_1 = first
        
        while temp_1 is not None:
            first_num += str(temp_1.data)
            temp_1 = temp_1.next
        
        # print(first_num)    
        
        ## converting second linked list into string
        temp_2 = second
        
        while temp_2 is not None:
            second_num += str(temp_2.data)
            temp_2 = temp_2.next
        
        # Addition of the two numbers
        
        c = int(first_num) + int(second_num)
        c_list = list(str(c))
        
        head = Node(c_list[0])
        temp = head
        
        # Making of the liked list of the answer
        for i in range(1, len(c_list)):
            node = Node(c_list[i])
        
            while temp.next is not None:
                temp = temp.next
            temp.next = node
                
        return head