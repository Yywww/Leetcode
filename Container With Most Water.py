class Solution(object):
	def maxArea(self, height):
		indexes=height.index(max(height))
		prevmax=0
		leftindex=[]
		rightindex=[]
		for i in range(indexes):
			if height[i]>prevmax:
				prevmax=height[i]
				leftindex.append(i)
			else:
				height[i]=0
		leftindex.append(indexes)

		heightr=height[::-1]
		indexes=heightr.index(max(height))
		prevmax=0
		for i in range(indexes):
			if heightr[i]>prevmax:
				prevmax=heightr[i]
				rightindex.append(i)
			else:
				heightr[i]=0
		rightindex.append(indexes)
		maxv=0
		lh=len(height)
		for i in leftindex:
			for j in rightindex:
				v=((lh-j-1)-i)*min(height[i],heightr[j])
				if v>maxv:
					maxv=v
		return maxv
a=Solution()
print a.maxArea([1,2,3])