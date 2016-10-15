
class Solution(object):
	def convert(self, s, numRows):
		if numRows==1:
			return s
		loop=2*numRows-2
		line=numRows-1
		news=''
		for i in range(numRows):
			for n in range(len(s)/loop+1):
				j=(n*loop+i)
				try:
					news+=s[j]
				except:
					break
				if i==0 or i==line:
					continue
				j=((n+1)*loop-i)
				try:
					news+=s[j]
				except:
					break

		return news


a=Solution()
print a.convert("abcdefgh",3)
