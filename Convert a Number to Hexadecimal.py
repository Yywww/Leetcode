class Solution(object):
	def toHex(self, num):
		dic={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
		if num==0:
		    return '0'
		if num<0:
			num=16**8+num
		digit=''

		while num>0:
			d=num%16
			if d>9:
				digit=dic[d]+digit
			else:
				digit=str(d)+digit
			num=num/16
		return digit
Solution().toHex(26)