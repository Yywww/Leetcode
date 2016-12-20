class Solution(object):
	def detectCycle(self, head):
		if head is None: return None
		a=head
		b=head
		c=head
		while a.next and b.next:
			a=a.next
			if b.next.next:
				b=b.next.next
			else:
				return None
			if a==b:
				while True:
					if a==c:
						return a
					a=a.next
					c=c.next

		return None