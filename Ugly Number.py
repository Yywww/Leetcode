class Solution(object):
	def isUgly(self, num):
		if num==0:
			return False
		while True:
			if num==1:
				return True
			if num%2 and num%3 and num%5:
				return False
			if num%2==0:
				num=num/2
			if num%3==0:
				num=num/3    		
			if num%5==0:
				num=num/5