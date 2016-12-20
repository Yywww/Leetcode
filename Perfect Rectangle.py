import collections
class Solution(object):
	def isRectangleCover(self, rectangles):
		pointset = collections.defaultdict(int)
		s=0
		for rect in rectangles:
			one=rect[0]
			two=rect[1]
			three=rect[2]
			four=rect[3]
			for point in [(one,two), (one,four),(three,two),(three,four)]:
				pointset[point]+=1
			s+=(four-two)*(three-one)
		temp=[]
		for i in pointset:
			if pointset[i]==1:
				temp.append(i)
			if pointset[i] not in (1,2,4):
				return False
		temp.sort()
		print temp
		if len(temp)!=4:
			return False
		print s
		ss=(temp[3][0]-temp[0][0])*(temp[3][1]-temp[0][1])
		if s!=ss:
			return False
		return True
print Solution().isRectangleCover([[0,0,1,1],[0,1,1,2],[0,2,1,3],[1,0,2,1],[1,0,2,1],[1,2,2,3],[2,0,3,1],[2,1,3,2],[2,2,3,3]])