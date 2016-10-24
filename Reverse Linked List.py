class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
    	l=[]
    	while head is not None:
    		l.append(head.val)
    		head=head.next
    	l=l[::-1]
    	head=ListNode(0)
    	curnode=head
    	for i in l:
    		curnode.next=ListNode(i)
    		curnode=curnode.next
    	return head.next