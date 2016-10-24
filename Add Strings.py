class Solution(object):
    def addStrings(self, num1, num2):
    	m=max(len(num1),len(num2))
    	num1=num1.rjust(m+1, '0')
    	num2=num2.rjust(m+1, '0')
    	carry=0
    	num3=''
    	for i in range(m+1):
    		n1=ord(num1[::-1][i])-48
    		n2=ord(num2[::-1][i])-48
    		n3=(n1+n2+carry)%10
    		carry=(n1+n2+carry)/10

    		num3=str(n3)+num3
    	if num3[0]=='0':
    		num3=num3[1:]
    	return num3
print Solution().addStrings("99","9")