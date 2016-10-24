class Solution(object):
    def longestPalindrome(self, s):
    	r=list(set(s))
    	n=0
    	for i in r:
    		n+=(s.count(i)/2)*2
    	if n<len(s):
    		n+=1
    	return n

print Solution().longestPalindrome("abccccdd")