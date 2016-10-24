class Solution(object):
    def firstUniqChar(self, s):
    	r=list(set(s))
    	print r
    	for i in range(len(s)):
    		t=s[i]
    		if t in r:
    			if s[i+1:].count(t)==0:
	    			return i
    			r.remove(t)
    			


print Solution().firstUniqChar('loveleetcode')