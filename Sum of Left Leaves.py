# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sumOfLeftLeaves(self, root):
		sum=0
		if root is None:
			return 0
		root=[root]
		while True:
			temp=[]
			for i in root:
				if i.left is not None: temp.append(i.left)
				if i.right is not None: temp.append(i.right) 
				if i.left is not None and i.left.left is None and i.left.right is None:
					sum+=i.left.val
			if temp==[]:
				return sum
				break
			root=temp

