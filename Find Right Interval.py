# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
	def findRightInterval(self, intervals):
		d=[]
		ans=[]
		l=len(intervals)
		intervals=[[i,intervals.index(i)] for i in intervals]
		intervals.sort(key=lambda x: x[0].start)
		for i in range(l):
			j=i+1
			k=-1
			while j<l:
				if intervals[i][0].end<=intervals[j][0].start:
					k=intervals[j][1]
					break
				j+=1
			ans.append(k)
		re=[0]*l
		for i in range(l):
			re[intervals[i][1]]=ans[i]
		return re

a=Interval(1,4)
b=Interval(2,3)
c=Interval(4,5)
print Solution().findRightInterval([b,a,c])