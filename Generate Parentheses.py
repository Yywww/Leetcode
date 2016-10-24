class Solution(object):
    def generateParenthesis(self, n):
    	solset=['(']
    	for i in range(2*n-1):
    		solset_temp=[]
    		for j in solset:
        		countleft  = j.count('(')
        		countright = j.count(')')
        		if countright==countleft:
        			solset_temp.append(j+'(')
        		elif (n-countleft)==0:
        			solset_temp.append(j+')')
        		else:
        			solset_temp.append(j+'(')
        			solset_temp.append(j+')')
        	solset=solset_temp
        return solset

print Solution().generateParenthesis(7)
