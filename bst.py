class Node:
    def __init__(self, key):
        self.rchild = None
        self.lchild = None
        self.key = key


class BST:
    def __init__(self, values=None) -> None:
        self.root = None
        if values is not None:
            for value in values:
                self._insert(self.root, value)

    def insert(self, key):
        self._insert(self.root, key)

    def _insert(self, curNode, key):
        if self.root is None:
            self.root = Node(key)
            return
        if key < curNode.key:
            if curNode.lchild is None:
                curNode.lchild = Node(key)
            else:
                curNode.lchild = self._insert(curNode.lchild, key)
        else:
            if curNode.rchild is None:
                curNode.rchild = Node(key)
            else:
                curNode.rchild = self._insert(curNode.rchild, key)
        return curNode

    def findNode(self, key):
        return self._search(self.root, key)

    def _search(self, curNode, key):
        if key == curNode.key:
            return curNode
        elif key < curNode.key and curNode.lchild is not None:
            return self._search(curNode.lchild, key)
        elif key > curNode.key and curNode.rchild is not None:
            return self._search(curNode.rchild, key)
        else:
            return None

    def print(self):
        self._print(self.root)

    def _print(self, root, space=0):
        distance = [10]
        if root is None:
            return
        space += distance[0]
        self._print(root.rchild, space)
        print()
        for i in range(distance[0], space):
            print(end=" ")
        print(root.key)
        self._print(root.lchild, space)

    def deleteNode(self, key):
        return self._deleteNode(self.root, key)

    def _deleteNode(self, curNode, key):
        if curNode is None:
            return curNode
        if curNode.key > key:
            curNode.lchild = self._deleteNode(curNode.lchild, key)
        elif curNode.key < key:
            curNode.rchild = self._deleteNode(curNode.rchild, key)
        else:
            if curNode.rchild is None and curNode != self.root:
                return curNode.lchild
            if curNode.lchild is None and curNode != self.root:
                return curNode.rchild
            cur = curNode.rchild
            while cur.lchild:
                cur = cur.lchild
            curNode.key = cur.key
            curNode.rchild = self._deleteNode(curNode.rchild, curNode.key)
        return curNode
