class Solution(object):
	def findLadders(self, beginWord, endWord, wordlist):
		path={beginWord:[beginWord]}
		queue=[beginWord]
		l=len(beginWord)
		discover=dict(zip(wordlist,[False]*len(wordlist)))
		while len(queue)>0:
			curword=queue[0]
			queue.pop(0)
			for i in wordlist:
				if discover[i]==False:
					e=0
					if sum([i[j]==curword[j] for j in range(l)])==1:
						discover[i]=True
						path[i]=path[curword]+[i]
						queue.append(i)
		print path
		print discover

Solution().findLadders("hit","cog",["hot","dot","dog","lot","log"])