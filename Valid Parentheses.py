class Solution(object):
	def isValid(self, s):
		l=[]
		for char in s:
			if char in ('(','[','{'):
				l.append(char)
				s=char
			if char==')':
				if s=='(':
					l.pop()
				else:
					return False
			if char==']':
				if s=='[':
					l.pop()
				else:
					return False   		
			if char=='}':
				if s=='{':
					l.pop()
				else:
					return False
			try:
				s=l[-1]
			except:
				pass
		if len(l)==0:
			return True
		else:
			return False

print Solution().isValid('([{})')