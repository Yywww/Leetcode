class Solution(object):
	def isPowerOfThree(self, n):
		if n<=0:
			return False
		if 10460353203%n==0:
			return True
		else:
			return False
print Solution().isPowerOfThree(27)