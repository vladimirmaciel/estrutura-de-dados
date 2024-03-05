class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    """ precurso em ordem simetrica """

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end=' ')
            self.simetric_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.simetric_traversal(node.right)
            print(') ', end=' ')
