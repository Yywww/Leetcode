class Solution(object):
	def primePalindrome(self, N):
		l = len(str(N))
		start = 10**(l//2-1+l%2)
		odd = True
		if N<=11:
			return min([i for i in [2,3,5,7,11] if i>=N])
		print(start)
		while True:
			starts = str(start)
			if int(starts[0])%2==0:
				# print(str(int(starts[0])+1))
				starts=str(int(starts[0])+1)+starts[1:]
				start = int(starts)
			if odd:
				num = int(starts+starts[:-1][::-1])
			else:
				num = int(starts+starts[::-1])
			if num>N and self.checkPrime(num):
				return num
			start+=1
			if len(str(start))>len(str(start-1)):
				if odd:
					odd = False
					start = start//10
				else:
					odd = True


	def checkPrime(self,num):
		i=3
		while i**2<=num:
			if num%i==0:
				return False
			i+=2
		return True
print(Solution().primePalindrome(11))