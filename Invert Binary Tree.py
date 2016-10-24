class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def invertTree(self, root):
		if root is None:
			return root
		root2=root
		root=[root]

		while len(root)>0:
			temp=[]
			for i in root:
				if i.left is not None: temp.append(i.left)
				if i.right is not None: temp.append(i.right)
				t=i.left
				i.left=i.right
				i.right=t
			root=temp
		return root2

Solution().invertTree(None)
