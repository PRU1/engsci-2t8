## linked list implementation

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None # points to null by default
class LL():
    def __init__(self):
        # store head node
        self.head = None 

    def get_i(self, i):
        x = 0
        cur = self.head 
        while x < i:
            cur = cur.next 
            x += 1
        return cur.data
        
    def append(self, value):
        # traverse to end of linkedlist and add a node
        newNode = Node(value) # create new node
        # case 1: head node is None
        if self.head == None:
            self.head = newNode

        else: 
            # find the last node
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
    def insert(self, value, i):
        newNode = Node(value)
        if i == 0:
            tmp = self.head
            self.head = newNode
            newNode.next = tmp # this can be done in two lines by the way
        else: 
            cur = self.head
            for i in range (i-1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
    def printLL(self):
        cur = self.head
        if cur == None:
            print("empty")
        while (cur != None):
            print(cur.data, " ", end="")
            cur = cur.next

# driver code
hi = LL()
hi.append(4)
hi.append(5)
print("hello")
hi.printLL()
print("\n")
hi.insert(5,2)
hi.printLL()
print(hi.get_i(2))
