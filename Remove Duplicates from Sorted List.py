# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		if head is None:
			return head
		c=ListNode(0)
		c.next=head
		while head.next is not None:
			if head.val==head.next.val:
				head.next=head.next.next
			else:
				head=head.next
		return c.next

a=ListNode(1)
# a.next=ListNode(1)
# a.next.next=ListNode(1)
c=Solution().deleteDuplicates(a)
print c.next

