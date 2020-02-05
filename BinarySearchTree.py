import Node


class BST():
	
	def __init__(self):
		self.rootNode = None

	def insert(self,data):
		if self.rootNode is None:
			self.rootNode = Node.Node(data)
		else:
			self.rootNode.insert(data)

	def remove(self, dataToRemove):
		if self.rootNode is not None:
			if self.rootNode.data == dataToRemove:
				tempNode = Node.Node(None)
				tempNode.leftChild = self.rootNode
				self.rootNode.remove(dataToRemove, tempNode)
			else:
				self.rootNode.remove(dataToRemove, None)

	def getMax(self):
		if self.rootNode is not None:
			return self.rootNode.getMax()

	def getMin(self):
		if self.rootNode:
			return self.rootNode.getMin()

	def traverseInOrder(self):
		if self.rootNode is not None:
			self.rootNode.traverseInOrder()
			
