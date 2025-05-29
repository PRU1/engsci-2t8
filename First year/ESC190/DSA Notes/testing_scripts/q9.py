class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

root = Node(1)
n4 = Node(4)
n5 = Node(5)
n7 = Node(7)

root.left = n4
root.right = n5
n5.left = n7

def sum(root):
    # do a depth first search.. let's try recursive
    yay = root.value
    visited = []
    visited.append(root)
    if root.left != None:
        yay += sum(root.left)
    if root.right != None:
        yay += sum(root.right)
    
    return yay

print(sum(root))




