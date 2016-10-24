class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		if root is None:
			return 0
		root=[root]
		n=1
		while True:
			temp=[]
			for i in root:
				if i.left is not None: temp.append(i.left)
				if i.right is not None: temp.append(i.right) 

			if temp==[]:
				return n
				break
			root=temp
			n+=1

			
a=TreeNode(10)
a.left=TreeNode(3)
a.left.left=TreeNode(4)
print Solution().maxDepth([])