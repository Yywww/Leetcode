class Solution:
	def findIntegers(self, num):
		if num==0:
			return 1
		res = [0]
		temp = [1]
		arrayLen = [1,2]
		arrayLow = [1,2]
		arrayUpp = [2,4]
		arrayfib = [1,1]
		i = 3
		while True:
			arrayLen.append(i)
			arrayUpp.append(2**i)
			fibo = arrayfib[-1]+arrayfib[-2]
			arrayfib.append(fibo)
			if arrayLow[-1]%2==0:
				arrayLow.append(arrayLow[-1]*2+1)
			else:
				arrayLow.append(arrayLow[-1]*2)
			if 2**i>num:
				break
			i+=1
		res = 0
		for i in range(len(arrayLen)):
			if num<arrayUpp[i]:
				if num>=arrayLow[i]:
					return sum(arrayfib[:i+1])+1
				else:
					s=sum(arrayfib[:i])+1+self.findIntegers(num-arrayUpp[i-1])
		return s



print(Solution().findIntegers(1040))