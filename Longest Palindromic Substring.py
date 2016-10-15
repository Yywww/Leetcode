class Solution(object):
	def longestPalindrome(self, s):
		if len(s)<=2:
			return s
		maxjodd=0
		maxi=None

		t='#'.join(s[i:i+1] for i in range(0, len(s), 1))
		t='#'+t+'#'
		# for odd
		back=t[0]
		mid=t[1]
		forth=t[2:]
		i=1
		while True:
			if min(len(back),len(forth))<maxjodd:
				break
			for j in range(min(len(back),len(forth))):
				if back[j]!=forth[j]:
					if j>=maxjodd:
						maxjodd=j
						maxiodd=i
					break
				if j==(min(len(back),len(forth))-1):
					if j>=maxjodd:
						maxjodd=j+1
						maxiodd=i
			back=mid+back
			mid=forth[0]
			forth=forth[1:]
			if len(forth)==0:
				break
			i+=1

		if maxjodd==1:
			return t[-2].replace('#','')
		print maxjodd
		return t[maxiodd-maxjodd:maxiodd+maxjodd+1].replace('#','')

					

s='abcda'
a=Solution()
b=a.longestPalindrome(s)
print b