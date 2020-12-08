class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

class BST(object):
    """ Binary search tree """
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node, value):
        """ Insert a node into binary search tree """
        if not node.value:
            node.value = value
        if value < node.value:
            node.left = node.left or Node()
            self.insert(node.left, value)
        elif value > node.value:
            node.right = node.right or Node()
            self.insert(node.right, value)       

    def delete(self, node, value, parent=None):
        """ Delete a node from binary search tree """
        if not node:
            return
        elif value < node.value:
            self.delete(node.left, value, parent=node)
        elif value > node.value:
            self.delete(node.right, value, parent=node)
        else:
            # Case 1: Node has no children, so remove node from its parent
            if not node.left and not node.right:
                if parent.left and node == parent.left:
                    parent.left = None
                else:
                    parent.right = None
            
            # Case 2: Node has two children, so start with the current node's right child, find that child's leftmost child, replace the current node's value with the leftmost child's value and call the deletion function on the current node's right child
            elif node.left and node.right:
                successor = node.right
                successor_parent = node
                while successor.left:
                    successor_parent = successor
                    successor = successor.left
                node.value = successor.value
                self.delete(successor, successor.value, parent=successor_parent)

            # Case 3: Node has one child, so replace the node with its child
            else:
                if parent.left and node == parent.left:
                    if node.left:
                        parent.left = node.left
                    if node.right:
                        parent.left = node.right
                else:
                    if node.left:
                        parent.right = node.left
                    if node.right:
                        parent.right = node.right

    def dfs(self, node):
        """ Depth-first search traversal """
        if not node:
            return []
        result = []
        if node.left:
            result = result + self.dfs(node.left)
        if node.value:
            result.append(node.value)
        if node.right:
            result = result + self.dfs(node.right)
        return result

    def bfs(self, node):
        """ Breadth-first search traversal """
        result = []
        nodelist = [node]

        while nodelist:
            next_nodelist = []
            for subnode in nodelist:
                result.append(subnode.value)
                if subnode.left:
                    next_nodelist.append(subnode.left)
                if subnode.right:
                    next_nodelist.append(subnode.right)
            nodelist = next_nodelist
        
        return result