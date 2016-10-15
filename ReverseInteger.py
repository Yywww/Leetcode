class Solution(object):
    def reverse(self, x):
    	s=str(x)
    	s=s[::-1]
    	while s.find('0')==0:
    		s=s[1:]
    	if s.find('-')!=-1:
    		s='-'+s
    		s=s[:-1]
    	if s=='':
    		return 0
    	if int(s)>2**31:
    	    return 0
    	return int(s)

a=Solution()
print a.reverse(123)