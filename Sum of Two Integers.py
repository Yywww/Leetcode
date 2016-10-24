class Solution(object):
	def getSum(self, a, b):

		if (a == 0): return b
		if (b == 0): return a
		if (a == 2147483647 and b == -2147483648): return -1
		flag = False
		if (a < 0 and b < 0):
			a = -a
			b = -b
			flag = True

		mask = 0xffffffff
		print bin(mask)
		print bin(-2)
		while (b != 0):
			a = a & mask
			b = b & mask
			print 'a=',bin(a),'b=',bin(b)
			carry = a & b & mask
			a = a ^ b
			b = (carry << 1) & mask
		return -a if flag else a

print Solution().getSum(13,-2)

