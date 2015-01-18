#!/usr/bin/python2

class BST(object):

    class Node(object):
        def __init__(self, val=None):
            self.left = None
            self.right = None
            self.data = val


    def __init__(self):
        self.root = None


    def _insert(self, root, val):
        """Insert a node under root"""
        if root == None:
            root = self.Node(val)
        else:
            if val < root.data:
                root.left = self._insert(root.left, val)
            else:
                root.right = self._insert(root.right, val)
        return root


    def insert(self, val):
        self.root = self._insert(self.root, val)


    def _print_inorder(self, root):
        """Print tree nodes with in-order traversal"""
        if root == None:
            return
        else:
            self._print_inorder(root.left)
            print root.data
            self._print_inorder(root.right)


    def print_inorder(self):
        self._print_inorder(self.root)


    def _max_height(self, root):
        if root == None:
            return 0
        else:
            return max(self._max_height(root.left), self._max_height(root.right)) + 1; 


    def _min_height(self, root):
        if root == None:
            return 0
        else:
            return min(self._min_height(root.left), self._min_height(root.right)) + 1; 


    def is_balanced(self):
        return self._max_height(self.root) - self._min_height(self.root) < 2

    
if __name__ == "__main__":
    bst = BST()

#    bst.insert(10)
#    bst.insert(5)
#    bst.insert(2)
#    bst.insert(4)
#    bst.insert(8)
#    bst.insert(1)

    bst.insert(10)
    bst.insert(8)
    bst.insert(5)
    bst.insert(12)
    bst.insert(13)

    bst.print_inorder()

    if bst.is_balanced():
        print "Tree is balanced"    
    else:
        print "Tree is not balanced"

