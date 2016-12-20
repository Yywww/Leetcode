class Solution(object):
	def isMatch(self, s, p):
		matrix=[[False for i in range(len(s)+1)] for j in range(len(p)+1)]
		matrix[0][0]=True
		for i in range(1,len(p)+1):
			for j in range(1,len(s)+1):
				if p[i-1]=='*':
					if matrix[i-2][j]==True:
						matrix[i][j]=True 
					if matrix[i-1][j]==True:
						matrix[i][j]=True
				if s[j-1]=='*':
					if matrix[i][j-2]==True:
						matrix[i][j]=True 
					if matrix[i][j-1]==True:
						matrix[i][j]=True 
				if p[i-1]==s[j-1] or s[j-1]=='.' or p[i-1]=='.' or (p[i-1]=='*' and (p[i-2]==s[j-1] or p[i-2]=='.')):
					if matrix[i-1][j-1]==True:
						matrix[i][j]=True 
		return matrix

print Solution().isMatch("ab", ".*")