class Solution:
	def findWords(self, board, words):
		self.t = Trie()
		self.t.make_trie(words)
		self.res = []
		self.board = board
		l1 = len(self.board)
		l2 = len(self.board)[0]
		# print(self.t.find_word('aa'))
		for i in range(len(board)):
			for j in range(len(board[0])):
				self.dfs((i,j),[(i,j)],board[i][j],l1,l2)
		return self.res

	def dfs(self,point,past,prefix,l1,l2):
		if self.t.find_word(prefix):
			if prefix not in self.res:
				self.res.append(prefix)
		nextletterloc = [(point[0]+1,point[1]),(point[0]-1,point[1]),(point[0],point[1]+1),(point[0],point[1]-1)]
		for (i,j) in nextletterloc:
			if i<0 or j<0 or i>=l1 or j>=l2:
				continue
			if (i,j) in past:
				continue
			new_prefix = prefix+self.board[i][j]
			if self.t.find_pre(new_prefix):
				self.dfs([i,j],past+[(i,j)],new_prefix,l1,l2)
		return

class Trie():
	def __init__(self):
		self._end = '*'
		self.trie = dict()

	def __repr__(self):
		return repr(self.trie)

	def show(self):
		print(self.trie)
	def make_trie(self, words):
		trie = dict()
		for word in words:
			temp_dict = trie
			for letter in word:
				temp_dict = temp_dict.setdefault(letter, {})
			temp_dict[self._end] = self._end
		self.trie = trie

	def find_pre(self, prefix):
		sub_trie = self.trie
		for letter in prefix:
			if letter in sub_trie:
				sub_trie = sub_trie[letter]
			else:
				return False
		return True
	def find_word(self, word):
		sub_trie = self.trie

		for letter in word:
			if letter in sub_trie:
				sub_trie = sub_trie[letter]
			else:
				return False
		else:
			if self._end in sub_trie:
				return True
			else:
				return False

	def add_word(self, word):
		if self.find_word(word):
			print("Word Already Exists")
			return self.trie

		temp_trie = self.trie
		for letter in word:
			if letter in temp_trie:
				temp_trie = temp_trie[letter]
			else:
				temp_trie = temp_trie.setdefault(letter, {})
		temp_trie[self._end] = self._end
		return temp_trie



print(Solution().findWords([["a","a"]],["aaa"]))
