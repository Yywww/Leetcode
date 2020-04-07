import os
import time

input_matrix = [
  [".","8","1",".","3","7","4",".","."],
  ["5","4","3","6","8","9","7","1","2"],
  [".","7",".","4",".","1","3","8","."],
  ["7","3","9","8","4","5","6","2","1"],
  ["8",".",".","1","7","6","9","3","4"],
  ["1","6","4","3","9","2","5","7","8"],
  [".","9","8","7",".","4","1","5","3"],
  ["3","1",".","9",".","8","2","4","7"],
  ["4",".","7",".","1","3","8",".","."]
]

def solve(dic):
	for i in range(9):
		for j in range(9):
			if dic[i][j] == ".":
				# loop though row
				row = []
				col = []
				sq  = []
				for n in range(9):
					if dic[i][n]!=".": row.append(dic[i][n])
					if dic[n][j]!=".": col.append(dic[n][j])

				x = int(i/3)
				y = int(j/3)
				for q in range(3):
					for w in range(3):
						point = dic[x*3+q][y*3+w]
						if point!=".": sq.append(point)
				total = row+col+sq
				total_number = list(set([int(e) for e in total]))
				poss = []
				for r in range(1,10,1):
					if r not in total_number:
						poss.append(r)
				print("lat:",str(i),",lng:",str(j),",possibility:",''.join([str(e) for e in poss]))
				


solve(input_matrix)





