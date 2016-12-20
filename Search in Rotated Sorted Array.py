class Solution(object):
	def search(self, nums, target):
		L=0
		R=len(nums)-1
		ma=nums[L]
		mi=nums[R]
		while R-L!=1:
			mid=(L+R)/2
			if nums[L]<nums[mid]:
				ma=nums[mid]
				L=mid
				continue
			if nums[R]>nums[mid]:
				mi=nums[mid]
				R=mid
				continue
		if target>=nums[0]:
			nums=nums[:R]
			c=0
		else:
			nums=nums[R:]
			c=R
		print nums,c
		L=0
		R=len(nums)-1
		while L<=R:
			mid=(L+R)/2+(L+R)%2
			if nums[mid]<target:
				L=mid+1
			elif nums[mid]>target:
				R=mid-1
			else:
				return mid+c
		return -1

print Solution().search([7,8,0,1,2,3,4,5,6],7)
