class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preorderTraversal(self, root):
		p = root
		stack = []
		ans = []
		while p or stack:
			while p:
				stack.append(p)
				ans.append(p.val)
				p = p.left
			p=stack.pop()
			p=p.right
		return ans

