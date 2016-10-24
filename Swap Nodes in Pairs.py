
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
		if head is None or head.next is None:
			return head
		dummy=ListNode(0)
		c=dummy
		while head is not None:
			c.next=ListNode(head.next.val)
			c.next.next=ListNode(head.val)
			try:
				c.next.next.next=ListNode(head.next.next.val)
			except:
				pass
			c=c.next.next
			head=head.next.next
			if head is None or head.next is None:
				break
		return dummy.next

    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next


def printLinkedList(head):
	while head is not None:
		print head.val
		head=head.next
	return

b=ListNode(1)
b.next=ListNode(2)
b.next.next=ListNode(3)
b.next.next.next=ListNode(4)

d=Solution().swapPairs(b)
printLinkedList(d)