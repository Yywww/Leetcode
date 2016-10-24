
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrderBottom(self, root):
		if root is None:
			return []
		root=[root]
		result=[]
		while True:
			temp=[]
			tempval=[]
			for i in root:
				tempval.append(i.val)
			for i in root:
				if i.left is not None: 
					temp.append(i.left)
				if i.right is not None: 
					temp.append(i.right) 
			result.append(tempval)
			if temp==[]:
				break
			root=temp
		return result[::-1]