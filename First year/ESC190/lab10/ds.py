class Queue:
    # queues are lifo
    def __init__(self):
        self.items = [] # is this like a constructor
    
    def add(self, item):
        self.items.insert(0, item)

    def get(self):
        return self.items.pop() # remove last element ? shouldn't it be first

    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

class Stack:
    # fifo
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def get(self):
        return self.items.pop() # remove last element
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
