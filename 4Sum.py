class Solution(object):
    def fourSum(self, nums, target):
		solset=[]
		nums.sort()
		l=len(nums)
		for i in range(l-3):
			for j in range(i+1,l-2):
				twoSum=nums[i]+nums[j]
				k,r=j+1,l-1
				remain=target-twoSum
				while (k < r):
					if remain==nums[k]+nums[r]:
						solset.append([nums[i],nums[j],nums[k],nums[r]])
					if remain>nums[k]+nums[r]:
						k+=1
					else:
						r-=1 

		solset=[list(x) for x in set(tuple(x) for x in solset)]
		return solset

print Solution().fourSum([-4,-3,-2,-1,0,0,1,2,3,4],0)