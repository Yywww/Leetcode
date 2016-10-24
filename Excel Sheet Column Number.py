class Solution(object):
    def titleToNumber(self, s):
    	dict={chr(i):(i-64) for i in range(ord('A'),ord('Z')+1)}
    	s=list(s)[::-1]
    	n=0
    	for i in range(len(s)):
    		n+=dict[s[i]]*(26**i)
    	return n
print Solution().titleToNumber('AAA')