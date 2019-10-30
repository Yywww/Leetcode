class Solution(object):
	def movesToChessboard(self, board):
		l = len(board)
		if len(board)%2==1:
			odd=True
		else:
			odd=False
		rowExample = board[0]
		rowReverse = [1-i for i in rowExample]
		colExample = [board[i][0] for i in range(len(board))]
		colReverse = [1-i for i in colExample]

		row1=[]
		row2=[]
		col1=[]
		col2=[]
		for i in range(len(board)):
			if (odd and sum(board[i]) not in [l//2,l//2+1]) or (not odd and sum(board[i])!=l//2):
				return -1
			if board[i]==rowExample:
				row1.append(i)
			elif board[i]==rowReverse:
				row2.append(i)
			else:
				return -1
		for j in range(len(board)):

			curCol = [board[i][j] for i in range(len(board))]
			if (odd and sum(curCol) not in [l//2,l//2+1]) or (not odd and sum(curCol)!=l//2):
				return -1
			if curCol==colExample:
				col1.append(j)
			elif curCol==colReverse:
				col2.append(j)
			else:
				return -1
		step = 0
		if odd:
			if len(row1)>len(row2):

				test = row1
			else:
				test = row2
			if len(test)!=len(board)//2+1:
				return -1
			for index in test:
				if index%2!=0:
					step+=1

			if len(col1)>len(col2):
				test = col1
			else:
				test = col2
			if len(test)!=len(board)//2+1:
				return -1
			for index in test:
				if index%2!=0:
					step+=1
			return step
		else:
			if len(row1)!=len(row2) or len(col1)!=len(col2):
				return -1
			c=0
			for index in col1:
				if index%2!=0:
					c+=1
			step+=min(c,len(col1)-c)
			c=0
			for index in row1:
				if index%2!=0:
					c+=1
			step+=min(c,len(row1)-c)
			return step


print(Solution().movesToChessboard([[1, 0], [1, 0]]))