class Solution(object):
	def isNumber(self, s):
		s=s.strip(' ')
		if len(s)==0:
			return False
		for i in s:
			if i not in ('1234567890.e-+'):
				return False
		if 'e' in s:
			if s.count('e')>1:
				return False
			int=s.split('e')[1]
			if not int:
				return False
			for i in int:
				if i not in ('1234567890-+'):
					return False
			if '-' in int or '+' in int:
				int=int[1:]
				if len(int)==0:
					return False
				for i in int:
					if i not in ('1234567890'):
						return False
			s=s[:s.index('e')]
		if '-' in s or '+' in s:
			s=s[1:]
			for i in s:
				if i not in ('1234567890.e'):
					return False
		if '.' in s:
			if len(s)==1:
				return False
			if s.count('.')>1:
				return False
		if len(s)==0:
			return False
		return True
print Solution().isNumber('8e+')	
