class Solution(object):
    def isPowerOfFour(self, num):
		if num<=0:
			return False
		if 65536%(num**0.5)==0:
			return True
		else:
			return False
print Solution().isPowerOfThree(27)