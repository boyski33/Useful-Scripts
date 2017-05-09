# a Node class and a BST class that creates a tree and has a method to insert new nodes
# need to make it self balancing 


class Node(object):
    count = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.data.__str__()

class BinarySearchTree(object):
    def __init__(self, *args):
        # set the root to be the average value in the list of nodes
        self.root = Node(sorted(args).pop(len(args)//2)) if args else None
        for n in args:
            self.insert_node(self.root, Node(n))

    # recursive; pretty straightforward 
    def insert_node(self, root, node):
        if type(node) is not Node:
            raise Exception("Not a Node object")
        if root is None:
            self.root = node
        elif node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                self.insert_node(root.left, node)
        elif node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                self.insert_node(root.right, node)
