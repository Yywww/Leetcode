class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		a=list(ransomNote)
		b=list(magazine)
		while len(a)>0:
			r=a[0]
			try:
				i=b.index(r)
			except:
				return False
			b.pop(i)
			a.pop(0)
		return True

print Solution().canConstruct('ab','acb')