class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		if lists==[] or lists==[[]]:
			return []
		minval=min([x.val for x in lists if x is not []])
		lists2=lists
		for x in lists:
			try:
				y=x.val
			except:
				continue
			if x.val==minval:
				if x.next is None:
					lists2.remove(x)
				else:
					lists2.append(x.next)
					lists2.remove(x)
				break
		a=ListNode(minval)
		a.next=Solution().mergeKLists(lists2)
		return a


def printLinkedList(head):
	while head!=[]:
		print head.val
		head=head.next
	return
b=ListNode(1)
b.next=ListNode(2)
c=ListNode(2)
c.next=ListNode(3)
e=ListNode(1)
e.next=ListNode(4)

d=Solution().mergeKLists([[]])
print d
printLinkedList(d)

