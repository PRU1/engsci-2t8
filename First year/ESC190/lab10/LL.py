# linked list implementation
class Node:
    def __init__(self, data):
        # store current point and pointer to next 
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    
    def insert(self, ind, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            if ind == 0:
                temp_head = self.head 
                self.head = new_node
                self.head.next = temp_head
            else:
                cur = self.head
                # get to end of linkedlist
                for i in range(ind-1):
                    cur = cur.next 
                cur.next = new_node 
                new_node.next = cur.next


    def print(self):
        cur = self.head
        while cur != None:
            print(cur.data, "->", end="")
            cur = cur.next

    def is_in(self, j):
        cur = self.head
        while cur:
            if cur.data == j:
                return True 
            cur = cur.next 
        return False
    
    def LL_size(self):
        counter = 0
        cur = self.head
        while cur:
            counter += 1
            cur = cur.next 
        return counter
        