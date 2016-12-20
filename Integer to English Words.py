class Solution(object):
	def __init__(self):
		self.numdic={0:'',1:' One',2:' Two',3:' Three',4:' Four',5:' Five',6:' Six',7:' Seven',8:' Eight',
		9:' Nine',10:' Ten',11:' Eleven',12:' Twelve',13:' Thirteen',14:' Fourteen',15:' Fifteen',
		16:' Sixteen',17:' Seventeen',18:' Eighteen',19:' Nineteen',20:' Twenty',30:' Thirty',
		40:' Forty',50:' Fifty',60:' Sixty',70:' Seventy',80:' Eighty',90:' Ninety'}
	def numberToWords(self, num):
		if num==0:
			return 'Zero'
		rets=''
		if num>=1000:
			rets+=Solution().numberToWordssmall(num%1000,'')
			num=num/1000
			if num>=1000:
				rets=Solution().numberToWordssmall(num%1000,' Thousand')+rets
				num=num/1000
				if num>=1000:
					rets=Solution().numberToWordssmall(num%1000,' Million')+rets
					num=num/1000
					rets=Solution().numberToWordssmall(num,' Billion')+rets
				else:
					rets=Solution().numberToWordssmall(num,' Million')+rets
			else:
				rets=Solution().numberToWordssmall(num,' Thousand')+rets
		else:
			return Solution().numberToWordssmall(num,'')[1:]
		return rets[1:]
	def numberToWordssmall(self, num, unit):
		if num==0:
			return ''
		if num in self.numdic:
			return self.numdic[num]+unit
		elif num<100:
			ty=num/10
			return self.numdic[ty*10]+self.numdic[num-ty*10]+unit
		else:
			ty=num/100
			return self.numdic[ty]+' Hundred'+Solution().numberToWordssmall(num%100,'')+unit

print Solution().numberToWords(123)
