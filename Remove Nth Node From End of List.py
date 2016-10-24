# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		b=ListNode(1.4)
		b.next=head
		i=0
		curnod=b
		nthnod=b
		while True:
			if curnod.next is None:
				nthnod.next=nthnod.next.next
				break
			curnod = curnod.next
			if i>=n:
				nthnod = nthnod.next
			i+=1
		return b.next

a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
# a.next.next.next=ListNode(4)
print a.val
print a.next.val
print a.next.next.val
print Solution().removeNthFromEnd(a,2)
print a.val
print a.next.val
# print a.next.next.val