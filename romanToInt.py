class Solution(object):
	def romanToInt(self, s):
		n=0
		while True:
			cur=s[0]
			if cur=='M':
				n+=1000
			if cur=='D':
				n+=500
			if cur=='C':
				n+=100
				if len(s)>1:
					if s[1]=='D' or s[1]=='M':
						n-=200
			if cur=='L':
				n+=50
			if cur=='X':
				n+=10
				if len(s)>1:
					if s[1]=='L' or s[1]=='C':
						n-=20
			if cur=='V':
				n+=5
			if cur=='I':
				n+=1
				if len(s)>1:
					if s[1]=='V' or s[1]=='X':
						n-=2
			if len(s)==1:
				break
			s=s[1:]			
		return n

a=Solution()
print a.romanToInt('DCXXI')