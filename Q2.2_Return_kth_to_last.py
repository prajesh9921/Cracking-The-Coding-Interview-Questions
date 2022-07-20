class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next

    def add_at_last(self, new_val):
        node = Node(new_val)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    # function to get kth element from last.

    def getNthFromLast(self,n):
        lst = []
        curr = self.head

        while curr is not None:
            lst.append(curr.data)
            curr = curr.next
        
        if len(lst) < n:
            return -1
        else:
            return lst[-n]


l1 = Linkedlist()
l1.head = Node(6)
l1.add_at_last(2)
l1.add_at_last(5)
l1.add_at_last(9)
l1.add_at_last(2)
l1.add_at_last(5)
l1.show()
print("")
c = l1.getNthFromLast(3)
print(c)

