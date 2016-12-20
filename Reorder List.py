class Solution(object):
	def reorderList(self, head):
		if head is None: return None
		l=1
		count=head
		while count.next:
			count=count.next
			l+=1
		halfl=l/2+1
		b=head
		while halfl>0:
			b=b.next
		rev_start=b
		c=Solution().reverse(b)
		while True
    def reverse(self, head):
        curt = None
        while head != None:
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt