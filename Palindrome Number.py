class Solution(object):
    def isPalindrome(self, x):
    	s=str(x)
    	t=s[::-1]
    	if s==t:
    		return True
    	else:
    		return False


a=Solution()
print a.isPalindrome(-2147483648)