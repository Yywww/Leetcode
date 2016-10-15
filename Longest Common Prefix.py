class Solution(object):
    def longestCommonPrefix(self, strs):
    	if len(strs)==0:
    		return ''
    	minlen=len(strs[0])
    	for s in strs:
    		if len(s)<minlen:
    			minlen=len(s)
    	while True:
    		prefixnow=strs[0][:minlen]
    		fail=0
    		for i in strs:
    			if i.find(prefixnow)!=0:
    				minlen-=1
    				fail=1
    				break
    		if fail==0:
    			break
    	return prefixnow

print Solution().longestCommonPrefix(['abc','ab','abd'])
