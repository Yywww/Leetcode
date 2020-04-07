class Solution(object):
	def findAnagrams(self, s, p):
		pFreq = {}
		sFreq = {}
		for i in [chr(x) for x in range(ord('a'), ord('z')+1)]:
			pFreq[i]=0
			sFreq[i]=0
		for char in p:
			pFreq[char]+=1

		l = len(p)
		for char in s[:l]:
			sFreq[char]+=1
		res = []
		for i in range(l,len(s)):
			if checkSameFreq(pFreq,sFreq):
				res.append(i-l)
			sFreq[s[i]]+=1
			sFreq[s[i-l]]-=1
		if checkSameFreq(pFreq,sFreq):
			res.append(len(s)-l)
		return res


def checkSameFreq(pFreq,sFreq):
	for key in pFreq:
		if pFreq[key]!=sFreq[key]:
			return False
	return True

ans = Solution().findAnagrams("abab","ab")
print(ans)