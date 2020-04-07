class Solution(object):
	def groupAnagrams(self, strs):
		m = {}
		for i in strs:
			sortedWord = ''.join(sorted([c for c in i]))
			if sortedWord not in m:
				m[sortedWord] = [i]
			else:
				m[sortedWord].append(i)
		res = []
		for key in m:
			res.append(m[key])

		return res