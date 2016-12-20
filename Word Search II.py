import collections
class Solution(object):
    def findWords(self, board, words):
    	w=len(board)
    	l=len(board[0])
    	wordDictnum = collections.defaultdict(list)
    	for i in range(w):
    		for j in range(l):
    			wordDictnum[board[i][j]]+=[[i,j]]
    	print wordDictnum
    	for word in words:
    		prev=[]
    		for i in range(len(word)):
    			for j in wordDictnum[word[i]]:
    				if prev==[]:
    					next.append(j)
    				else:
    					if j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1] for [x,y] in prev]



Solution().findWords(["oaan","etae","ihkr","iflv"],["oath","pea","eat","rain"])