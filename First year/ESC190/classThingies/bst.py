class MySetSlow:
    def __init__(self):
        self.data=[]
    def insert(self, x):
        if x not in self.data:
            self.data.append(x)
    def is_in(self,x):
        return x in self.data

# this implementation is slow. O(n) insertion, O(n) is_in, O(n) deletion :(

class MyDict:
    def __init__(self):
        self.data={}
    def insert(self, x, value):
        if x not in self.data:
            self.data.append((x,value))
    def is_in(self, x, k):
        for x, val in self.data:
            if k == x:
                return True
        return False
    def get(self, x):
        for k, val in self.data: # O(n), we can do betterrrrr
            if k==x:
                return val 
        return None
