class Solution(object):
	def threeSum(self, nums):
		solset=[]
		newnums=list(set(nums))
		for i in newnums:
			if nums.count(i)>1:
				if -2*i in nums:
					solset.append([i,i,-2*i])
		if [0,0,0] in solset:
			solset.remove([0,0,0])
		if nums.count(0)>2:
			solset.append([0,0,0])
		
		l=len(newnums)
		for i in range(l-2):
			for j in range(i+1,l-1):
				twosum=newnums[i]+newnums[j]
				if -twosum in newnums[j+1:]:
					solset.append([newnums[i],newnums[j],-twosum])
		return solset
