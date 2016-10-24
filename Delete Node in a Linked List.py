# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteNode(self, node):
		while True:
			node.val=node.next.val
			if node.next.next is None:
				node.next=None
				return
			else:
				node=node.next


a=ListNode(0)
a.next=ListNode(1)
Solution().deleteNode(a)
print a.val