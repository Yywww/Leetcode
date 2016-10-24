class Solution(object):
	def isHappy(self, n):
		l=[]
		while True:
			n=sum([int(i)**2 for i in str(n)])
			if n==1:
				return True
			if n in l:
				return False
			l.append(n)