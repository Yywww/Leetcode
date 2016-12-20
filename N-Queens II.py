class Solution(object):
	def solveNQueens(self, n):
		S=[[i] for i in range(n)]
		c=1
		while c<n:
			c+=1
			temp=[]
			for i in S:
				l=len(i)
				for j in range(n):
					if j not in i and j not in [i[r]+l-r for r in range(l)]+[i[r]-l+r for r in range(l)]:
						temp.append(i+[j])
			S=temp
			
		return len(S)
print Solution().solveNQueens(5)