# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		if p is None and q is None:
			return True
		if p is None or q is None:
			return False
		p=[p]
		q=[q]
		while True:
			temp_p=[]
			temp_q=[]
			for i in range(len(p)):
				if p[i].val!=q[i].val:
					return False
				if p[i].left is not None and q[i].left is not None:
						temp_q.append(q[i].left)
						temp_p.append(p[i].left)
				elif p[i].left is None and q[i].left is None:
					pass
				else:
					return False
				if p[i].right is not None and q[i].right is not None:
						temp_q.append(q[i].right)
						temp_p.append(p[i].right)
				elif p[i].right is None and q[i].right is None:
					pass
				else:
					return False
			p=temp_p
			q=temp_q
			if len(temp_p)==0:
				return True