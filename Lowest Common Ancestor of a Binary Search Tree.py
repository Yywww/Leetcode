# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		root={root:[root]}
		p_path=None
		q_path=None
		while True:
			temp={}
			for i in root.keys():
				if i.left is not None: 
					temp[i.left]=root[i]+[i]
				if i.right is not None: 
					temp[i.right]=root[i]+[i]
			root=temp
			if p in root.keys():
				p_path=root[p]
			if q in root.keys():
				q_path=root[q]
			if p_path is not None and q_path is not None:
				break
		for i in q_path:
			if i in p_path:
				common=i
			else:
				break
		return common

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)


a.left=b
b.left=d
b.right=e
a.right=c

print Solution().lowestCommonAncestor(a,c,e).val