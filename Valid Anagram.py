class Solution(object):
    def isAnagram(self, s, t):
    	if len(s)!=len(t):
    		return False
    	r=list(set(s))
    	for i in r:
    		if s.count(i)!=t.count(i):
    			return False
    	return True