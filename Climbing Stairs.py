class Solution(object):
	def climbStairs(self, n):
		x=(((1+5**(.5))/2)**(n+1)-((1-5**(.5))/2)**(n+1))/5**(.5)
		# a1=1
		# a2=1
		# c=0
		# while c<n:
		# 	a1=a1+a2
		# 	a1,a2=a2,a1
		# 	c+=1
		# 	print a1
		return int(x)

print Solution().climbStairs()