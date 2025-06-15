class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        '''inserts new node in the binary tree'''
        if self.root is None:
            self.root = Node(data)
        
        else:
            if data > self.root.data:
                self._insert(self.root, data)
            elif data < self.root.data:
                self._insert(self.root, data)
            
    def _insert(self, node: Node, data):
        '''auxiliar function to insert nodes in the tree'''
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(node.left, data)            
