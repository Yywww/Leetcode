# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
    	firstnode=ListNode(0)
    	lastnode=firstnode
    	while l1 is not None or l2 is not None:
    		if l1 is None:
    			lastnode.next=l2
    			break
    		elif l2 is None:
    			lastnode.next=l1
    			break
    		elif l2.val<l1.val:
    			curnod=l2
    			l2=l2.next
    		else:
    			curnod=l1
    			l1=l1.next
    		lastnode.next=curnod
    		lastnode=curnod
    	return firstnode.next	
        
a=ListNode(1)
b=ListNode(2)
c=Solution().mergeTwoLists(a,b)
print c.val
print c.next.val
