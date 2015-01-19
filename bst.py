#!/usr/bin/python2

import sys

class BST(object):

    class Node(object):
        def __init__(self, val=None):
            self.left = None
            self.right = None
            self.data = val
            self.x = 0
            self.y = 0


    def __init__(self):
        self.root = None


    def _insert(self, root, val):
        if root == None:
            root = self.Node(val)
        else:
            if val < root.data:
                root.left = self._insert(root.left, val)
            else:
                root.right = self._insert(root.right, val)
        return root


    def insert(self, val):
        """Insert a value into bst"""
        if type(val) == int:
            self.root = self._insert(self.root, val)


    def _print_tree(self, root, order):
        if root == None:
            return
        else:
            if order == "INORDER":
                self._print_tree(root.left, order)
                print root.data,
                self._print_tree(root.right, order)
            elif order == "PREORDER":
                print root.data,
                self._print_tree(root.left, order)
                self._print_tree(root.right, order)
            elif order == "POSTORDER":
                self._print_tree(root.left, order)
                self._print_tree(root.right, order)
                print root.data,


    def print_tree(self, order="INORDER"):
        """Print tree nodes with in/pre/post-order traversal"""
        if order == "INORDER" or order == "PREORDER" or order == "POSTORDER":
            print order + ": ",
            self._print_tree(self.root, order)
            print


    def print_level(self):
        if not self.root:
            return            
        queue = []
        queue.append(self.root)
        counter = 1
        while len(queue) > 0:
            temp = counter
            counter = 0
            for i in range(temp):
                node = queue.pop(0)
                print str(node.data),
                if node.left:
                    queue.append(node.left)
                    counter += 1
                if node.right:
                    queue.append(node.right)
                    counter += 1
            print   # Go to next level


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


    @classmethod
    def _is_bst(cls, root, lower, upper):
        if root == None:
            return True
        else:
            if root.data < lower or root.data > upper:
                return False
            return cls._is_bst(root.left, -float("inf"), root.data - 1) and cls._is_bst(root.right, root.data, float("inf"))

    @classmethod 
    def is_bst(cls, root):
        """Check if a binary tree is a binary search tree or not"""  
        return cls._is_bst(root, -float("inf"), float("inf"))

    
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
    bst.insert(5)
    bst.insert(12)
    bst.insert(13)

    bst.print_tree("INORDER")
    bst.print_level()

    if bst.is_balanced():
        print "Tree is balanced"    
    else:
        print "Tree is not balanced"

    if BST.is_bst(bst.root):
        print "Is a bst"
    else:
        print "Not a bst"
