# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def hasCycle(self, head):
		if head is None: return False
		a=head
		b=head
		while a.next and b.next:
			a=a.next
			if b.next.next:
				b=b.next.next
			else:
				return False
			if a==b:
				print a.val,b.val
				return True
		return False

		