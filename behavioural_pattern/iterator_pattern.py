class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.curr = None

    def __iter__(self):
        self.curr = self.head
        return self
    
    def __next__(self):
        if self.curr is None:
            raise StopIteration
        else:
            node = self.curr
            self.curr = self.curr.next
            return node.val
        

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
myList = LinkedList(head)

for n in myList:
    print(n)