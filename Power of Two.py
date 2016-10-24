class Solution(object):
    def isPowerOfTwo(self, n):
		if n<=0:
			return False
		if 2147483648%n==0:
			return True
		else:
			return False