# time complexity is O(1)
# using two stacks 

from collections import deque

class stack:
    def __init__(self):
        self.s = deque()
        self.s1 = deque()

    def push(self,x):
        if len(self.s) == 0:
            self.s.append(x)
            self.s1.append(x)
        else:
            self.s.append(x)
            if (self.s1[-1] >= self.s[-1]):
                self.s1.append(x)
        print(self.s)
                
    def pop(self):
        if len(self.s) == 0:
            return -1
        
        elif (self.s[-1] == self.s1[-1]):
            self.s1.pop()
        self.s.pop()
        
        print(self.s)
        

    def getMin(self):
        if len(self.s) == 0:
            return -1
        
        c = self.s1[-1]
        return c
    
    
stack = stack()
lst = [1 ,2 ,1 ,3 ,2 ,3 ,1 ,1 ,3]
for i in lst:
    stack.push(i)
    
stack.getMin()