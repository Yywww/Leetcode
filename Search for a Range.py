class Solution(object):
	def searchRange(self, nums, target):
		L=0
		R=len(nums)-1
		while True:
			mid=(L+R+1)/2
			if nums[mid]>=target and nums[mid-1]>=target:
				R=mid-1
			else:
				L=mid
			if L==R:
				return L
			if L>R:
				return [-1]


print Solution().searchRange([1,2,3,3,3,4,5],3)