class Solution(object):
	def intToRoman(self, num):
		s=str(num)
		ss=''
		s=s[::-1]
		try:
			s3=int(s[3])
			if s3==1:
				ss+='M'
			elif s3==2:
				ss+='MM'	
			elif s3==3:
				ss+='MMM'
		except:
			pass
		try:
			s2=int(s[2])
			if s2==1:
				ss+='C'
			elif s2==2:
				ss+='CC'	
			elif s2==3:
				ss+='CCC'
			elif s2==4:
				ss+='CD'
			elif s2==5:
				ss+='D'
			elif s2==6:
				ss+='DC'
			elif s2==7:
				ss+='DCC'
			elif s2==8:
				ss+='DCCC'
			elif s2==9:
				ss+='CM'
		except:
			pass



		try:
			s1=int(s[1])
			if s1==1:
				ss+='X'
			elif s1==2:
				ss+='XX'	
			elif s1==3:
				ss+='XXX'
			elif s1==4:
				ss+='XL'
			elif s1==5:
				ss+='L'
			elif s1==6:
				ss+='LX'
			elif s1==7:
				ss+='LXX'
			elif s1==8:
				ss+='LXXX'
			elif s1==9:
				ss+='XC'
		except:
			pass

		s0=int(s[0])
		if s0==1:
			ss+='I'
		elif s0==2:
			ss+='II'	
		elif s0==3:
			ss+='III'
		elif s0==4:
			ss+='IV'
		elif s0==5:
			ss+='V'
		elif s0==6:
			ss+='VI'
		elif s0==7:
			ss+='VII'
		elif s0==8:
			ss+='VIII'
		elif s0==9:
			ss+='IX'
		return ss

a=Solution()
print a.intToRoman(1)