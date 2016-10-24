class Solution(object):
    def reverseString(self, s):
    	r=list(s)
    	for i in range(len(r)/2):
    		tmp=r[i]
    		r[i]=r[-i-1]
    		r[-i-1]=tmp
        return ''.join(r)