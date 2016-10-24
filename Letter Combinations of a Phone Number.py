class Solution(object):
	def letterCombinations(self, digits):
		if digits=='':
			return []
		dictnum2abc = { 2:['a','b','c'],
						3:['d','e','f'],
						4:['g','h','i'],
						5:['j','k','l'],
						6:['m','n','o'],
						7:['p','q','r','s'],
						8:['t','u','v'],
						9:['w','x','y','z'],}
		dictnum2num = {2:3,3:3,4:3,5:3,6:3,7:4,8:3,9:4}
		le = len(digits)
		curlist=[0]*le
		n=0
		limit=1
		digits=[int(i) for i in digits]
		for i in digits:
			limit*=dictnum2num[i]
		limit-=1
		l=[]
		for i in digits:
			l.append(dictnum2abc[i])
		l=tuple(l)
		str=''
		for j in range(le):
			str+=l[j][0]
		allcomb=[str]	

		while n<limit:
			str=''
			curlist[0]+=1
			for i in range(le):
				if curlist[i]==4:
					curlist[i]=0
					curlist[i+1]+=1
				elif curlist[i]==3:
					if digits[i] in (9,7):
						continue
					curlist[i]=0
					curlist[i+1]+=1
			for j in range(le):
				str+=l[j][curlist[j]]
			allcomb.append(str)	
			n+=1
		return allcomb

print Solution().letterCombinations('3459')