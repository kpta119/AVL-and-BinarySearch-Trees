class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLtree:
    def __init__(self,  values=None):
        self.root = None
        if values is not None:
            for value in values:
                self.insert(self.root, value)

    def insert(self, currentNode, value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = TreeNode(value)
            else:
                currentNode.left = self.insert(currentNode.left, value)
        else:
            if currentNode.right is None:
                currentNode.right = TreeNode(value)
            else:
                currentNode.right = self.insert(currentNode.right, value)

        currentNode.height = 1 + max(self.getHeight(currentNode.left), self.getHeight(currentNode.right))

        balance = self.getHeight(currentNode.left) - self.getHeight(currentNode.right)

        #Left Left
        if balance > 1 and value < currentNode.left.value:
            return self.rightRotate(currentNode)

        #Right Right
        if balance < -1 and value > currentNode.right.value:
            return self.leftRotate(currentNode)


        #Left Right
        if balance > 1 and value > currentNode.left.value:
            currentNode.left = self.leftRotate(currentNode.left)
            return self.rightRotate(currentNode)


        #Right Left
        if balance < -1 and value < currentNode.right.value:
            currentNode.right = self.rightRotate(currentNode.right)
            return self.leftRotate(currentNode)
        return currentNode

    def getHeight(self, currentNode):
        if currentNode is None:
            return 0
        return currentNode.height

    def leftRotate(self, currentNode):
        if currentNode is self.root:
            self.root = currentNode.right
        if currentNode.right is not None:
            right = currentNode.right
            currentNode.right = right.left
            right.left = currentNode

            #Update height
            currentNode.height = 1 + max(self.getHeight(currentNode.left), self.getHeight(currentNode.right))
            right.height = 1 + max(self.getHeight(right.left), self.getHeight(right.right))
            return right

    def rightRotate(self, currentNode):
        if currentNode is self.root:
            self.root = currentNode.left
        if currentNode.left is not None:
            left = currentNode.left
            currentNode.left = left.right
            left.right = currentNode

            #Update height
            currentNode.height = 1 + max(self.getHeight(currentNode.left), self.getHeight(currentNode.right))
            left.height = 1 + max(self.getHeight(left.left),self.getHeight(left.right))
            return left

    def findNode(self, value):
        return self._findNode(self.root, value)

    def _findNode(self, currentNode, value):
        if value == currentNode.value:
            return currentNode
        elif value < currentNode.value and currentNode.left is not None:
            return self._findNode(currentNode.left, value)
        elif value > currentNode.value and currentNode.right is not None:
            return self._findNode(currentNode.right, value)
        else:
            return None

    def print(self, root, space=0):
        distance = [10]
        if root is None:
            return

        space += distance[0]

        self.print(root.right, space)

        print()
        for i in range(distance[0], space):
            print(end=" ")
        print(root.value)

        self.print(root.left, space)
