class Solution(object):
	def lengthOfLongestSubstring(self, s):
		ls=''
		maxlen=0
		for x in str(s):
			if x not in ls:
				ls+=x
				mlen=len(ls)
				if maxlen<mlen:
					maxlen=mlen 
			else:
				ls=ls.split(x)[1]
				ls+=x
		return maxlen