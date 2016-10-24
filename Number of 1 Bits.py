class Solution(object):
	def hammingWeight(self, n):
		s=0
		while n>0:
			s+=n%2
			n=n/2
		return s

print Solution().hammingWeight(-1)