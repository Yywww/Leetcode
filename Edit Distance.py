class Solution(object):
	def minDistance(self, word1, word2):
		l1=len(word1)
		l2=len(word2)
		matrix = [[0 for i in range(l1+1)] for j in range(l2+1)]
		for i in range(l1+1):
			matrix[0][i]=i
		for j in range(l2+1):
			matrix[j][0]=j
		for i in range(l2):
			for j in range(l1):
				matrix[i+1][j+1]=min([matrix[i+1][j]+1,matrix[i][j+1]+1,matrix[i][j]+(0 if word1[j]==word2[i] else 1)])
		return matrix[l2][l1]



print Solution().minDistance("a","ab")
