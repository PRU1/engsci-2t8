class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, elem):
        self.data.append(elem)
    
    def pop(self):
        # ret_val = self.data[-1]
        # return ret_val
        return self.data.pop()


if __name__=="__main__":
    s = Stack()
    s.push(5)
    s.push(10)
    print(s.pop())
    s.push(15)
    print(s.pop())