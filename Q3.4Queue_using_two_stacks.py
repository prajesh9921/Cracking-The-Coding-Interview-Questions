from collections import deque

class Queue:
    
    def __init__(self):
        self.s = []
        self.s1 = []
    
    def enqueue(self, X):
        
        while len(self.s) != 0:
            self.s1.append(self.s[-1])
            self.s.pop()
            
        self.s.append(X)
        
        while len(self.s1) != 0:
            self.s.append(self.s1[-1])
            self.s1.pop()
        
        
    def dequeue(self):
        if len(self.s) == 0:
            return -1
            
        c = self.s[-1]
        self.s.pop()
        return c