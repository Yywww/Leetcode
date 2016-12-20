class Solution(object):
	def divide(self, dividend, divisor):
		if dividend<0 and divisor<0:
			f=1
		elif dividend>0 and divisor>0:
			f=1
		else:
			f=-1
		dividend=abs(dividend)
		divisor=abs(divisor)
		n=[]
		d=[]
		a=1
		while divisor<=dividend:
			d.append(a)
			n.append(divisor)
			divisor=divisor+divisor
			a=a+a
		r=0
		while len(d)>0:
			if n[-1]<=dividend:
				dividend-=n[-1]
				r+=d[-1]
			d.pop()
			n.pop()
		if f==1: return r
		else: return -r


print Solution().divide(-2,1)