class Solution(object):
	def numDecodings(self, s):
		if not s: return 0
		t=s.replace('10','').replace('20','')
		l=len(t)
		if '0' in t:
			return 0
		if l<=1:
			return 1
		if l==2:
			return 2 if int(t)<=26 else 1
		D={}
		D[1]=1
		D[2]=2 if int(t[:2])<=26 else 1
		i=3
		while i<=l:
			if int(t[i-2:i])<=26:
				D[i]=D[i-1]+D[i-2]
			else:
				D[i]=D[i-1]
			i+=1
		return D[l]
print Solution().numDecodings("111")