# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		path=[]
		n=0
		cur=head
		while n<k:
			path.append(cur)
			cur=cur.next
			if cur.next is None:
				break
		# 	n+=1
		# if cur.next is None:
		# 	return
		nextround=cur
		path=path[::-1]

		for i in range(len(path)-1):
			path[i].next=path[i+1]
		path[len(path)-1].next=nextround
		print head.val
		head=path[0]



a=ListNode(8)
a.next=ListNode(7)
a.next.next=ListNode(6)

Solution().reverseKGroup(a,2)
print a.val
print a.next.val
# print a.next.next.val    	
