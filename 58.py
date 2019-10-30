class Solution:
	def lengthOfLastWord(self, s):
		l = len(s)
		c = 0
		for i in range(l):
			j = l-i-1
			if (s[j]==" ") & (c>0):
				break
			elif s[j]==" ":
				continue
			else:
				c+=1
		return c

print(Solution().lengthOfLastWord("b a "))