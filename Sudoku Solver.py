class Solution():
	def solveSudoku(self, board):
		boardmatrix=[[int(i) if i!='.' else i for i in j] for j in board]
		for h in range(30):
			self.boardmatrixpos=[[[] for i in j] for j in board]
			for j in range(9):
				for i in range(9):
					if boardmatrix[j][i]=='.':
						no=boardmatrix[j]+[boardmatrix[x][i] for x in range(9)]
						for x in boardmatrix[(j/3)*3:(j/3)*3+3]:
							no+=x[(i/3)*3:(i/3)*3+3]
						self.boardmatrixpos[j][i]=[x for x in range(1,10) if x not in no]
			for i in range(9):
				for j in range(9):
					if len(self.boardmatrixpos[i][j])==1:
						print 'Solve!'
						boardmatrix[i][j]=self.boardmatrixpos[i][j][0]
						self.update(i,j,self.boardmatrixpos[i][j][0])
			for j in range(9):
				pos=[y for x in [self.boardmatrixpos[x][j] for x in range(9)] for y in x]
				for i in range(1,10):
					if pos.count(i)==1:
						for k in range(9):
							if i in self.boardmatrixpos[k][j]:
								boardmatrix[k][j]=i
								print 'Solve!'
								self.update(k,j,i)
			for j in range(9):
				pos=[y for x in self.boardmatrixpos[j] for y in x]
				for i in range(1,10):
					if pos.count(i)==1:
						for k in range(9):
							if i in self.boardmatrixpos[j][k]:
								boardmatrix[j][k]=i
								print 'Solve!'
								self.update(j,k,i)
			for b in range(3):
				for c in range(3):
					pos=[y for x in self.boardmatrixpos[b*3:b*3+3] for y in x[c*3:c*3+3]]
					for i in range(1,10):
						if pos.count(i)==1:
							for d in range(3):
								for e in range(3):				
									if i in self.boardmatrixpos[b*3+d][c*3+e]:
										boardmatrix[b*3+d][c*3+e]=i
										print 'Solve!'
										self.update(b*3+d,c*3+e,i)					

		print boardmatrix

	def update(self,i,j,v):
		for m in self.boardmatrixpos[i]:
			if v in m:
				m.remove(v)
		for m in [self.boardmatrixpos[x][j] for x in range(9)]:
			if v in m:
				m.remove(v)
		for m in self.boardmatrixpos[(i/3)*3:(i/3)*3+3]:
			for n in m[(j/3)*3:(j/3)*3+3]:
				if v in n:
					n.remove(v)

		


board=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
Solution().solveSudoku(board)