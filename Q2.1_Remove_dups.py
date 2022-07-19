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

    # function to remove duplicates from the linked list.

    def removeDuplicates(self):

        dict = {}
        curr = self.head
        prev = None

        while curr is not None:
            if curr.data not in dict.keys():
                dict[curr.data] = 1
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next

        return self.head


l1 = Linkedlist()
l1.head = Node(6)
l1.add_at_last(2)
l1.add_at_last(5)
l1.add_at_last(9)
l1.add_at_last(2)
l1.add_at_last(5)
l1.show()
print("")
l1.removeDuplicates()
l1.show()
l1.show()
