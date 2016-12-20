
class Solution(object):
	def findKthNumber(self, n, k):
		numstr=''
		if n<10:
			return k
		d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
		for i in range(10):
			if n>9*10**i:
				for j in range(1,10):
					d[j]+=10**i
				n-=9*10**i
			else:
				for j in range(1,10):
					if n>10**i:
						d[j]+=10**i
						n-=10**i
					else:
						d[j]+=n
						n=0
						break
		i=1
		while True:
			if k>d[i]:
				k-=d[i]
				i+=1
			else:
				numstr+=str(i)
				break

		while k>1:
			if k==1:
				return int(numstr)
			else:
				k-=1
			n=d[i]-1
			d={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
			for i in range(10):
				if n>10**(i+1):
					for j in range(10):
						d[j]+=10**i
					n-=10**(i+1)
				else:
					for j in range(10):
						if n>10**i:
							d[j]+=10**i
							n-=10**i
						else:
							d[j]+=n
							n=0
							break
			i=0
			while True:
				if k>d[i]:
					k-=d[i]
					i+=1
				else:
					numstr+=str(i)
					break
		return int(numstr)
print Solution().findKthNumber(13,3)


