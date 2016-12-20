class Solution(object):
	def moveZeroes(self, nums):
		try:
			y=nums.index(0)
		except:
			return
		l=len(nums)
		while True:
			y=nums.index(0)
			x=y+1
			while x<l:
				if nums[x]!=0:
					nums[x],nums[y]=nums[y],nums[x]
					break
				if x==l-1:
					return
				x+=1
			if x>=l:
				return

a=[1]
print Solution().moveZeroes(a)
print a
