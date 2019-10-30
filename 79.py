class Solution:
	def exist(self, board, word):
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j]==word[0]:
					if self.dfs(board,word[1:],i,j,[(i,j)]):
						return True
		return False


	def dfs(self,board,word,x,y,path):
		if word == '':
			return True
		for (i,j) in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
			if i<0 or j<0 or i>=len(board) or j>= len(board[0]):
				continue
			if (i,j) in path:
				continue
			if board[i][j] == word[0]:
				if self.dfs(board,word[1:],i,j,path+[(i,j)]):
					return True
		return False
		
print(Solution().exist([["a","a"]],"aaa"))