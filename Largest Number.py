class Solution:
	def largestNumber(self, nums):
		m=max([len(str(i)) for i in nums])
		print m
		new=[int(str(i)+(m-len(str(i)))*str(i)[-1]) for i in nums]
		print new
		D={}
		for i in range(len(nums)):
			D[new[i]]=nums[i]
		new.sort(reverse=True)
		s=''
		for i in new:
			s+=str(D[i])
		return s

print Solution().largestNumber([121,12])