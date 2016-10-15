class Solution(object):
    def myAtoi(self, str):
       	neg=0
    	if str.find('-')!=-1:
    		neg=1
    	str=''.join([char for char in str if char in '1234567890.'])
    	if str=='' or str=='.':
    		return 0

    	s=str.split('.')[0]
    	if s.find('-')!=-1:
    		neg=1
    	while s[0]=='0':
    		s=s[1:]
    	if neg==1:
    		return -int(s)
    	else:
    		return int(s)

a=Solution()
print a.myAtoi('')