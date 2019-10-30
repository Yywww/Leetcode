class Solution:
	def xorGame(self, nums):
		nums = sorted(nums)
		# print(nums)
		self.save = {}
		s = 0
		for i in nums:
			s^=i
		return self.game(nums,s)

	def game(self,nums,xorsum):
		if len(nums)%2==1 and xorsum!=0:
			return False
		if tuple(nums) in self.save:
			return self.save[tuple(nums)]
		if xorsum==0:
			return True
		if len(nums)==0:
			self.save[tuple(nums)] = True
			return True
		lasti = -1
		for i in range(len(nums)):
			if i==lasti:
				continue
			if xorsum^nums[i]!=0:
				res = self.game(nums[0:i]+nums[i+1:],xorsum^nums[i])
				if res==False:
					self.save[tuple(nums)] = True
					return True
			lasti=i
		self.save[tuple(nums)] = False
		return False


print(Solution().xorGame([7899,3983,2534,4442,5497,1789,1014,726,3780,7077,3198,5692,4609,1157,4369,7043,4811,8094,1093,3230,3359]))
# # print(Solution().xorGame([1,1,2,2,3,5,7,8,9]))
# # print(Solution().xorGame([1,1,2,2,3,5,7,8]))
# # print(Solution().xorGame([1,1,2,2,3,5,7,9]))
# # print(Solution().xorGame([1,1,2,2,3,5,8,9]))
# # print(Solution().xorGame([1,1,2,2,3,7,8,9]))
# # print(Solution().xorGame([1,1,2,2,5,7,8,9]))
# # print(Solution().xorGame([1,1,2,3,5,7,8,9]))
# # print(Solution().xorGame([1,2,2,3,5,7,8,9]))
# for i in range(1,10):
# 	for j in range(1,10):
# 		for k in range(1,10):
# 			for l in range(1,10):
# 				# for m in range(1,10):
# 					if Solution().xorGame([i,j,k,l]):
# 						print(i^j^k^l,[i,j,k,l],Solution().xorGame([i,j,k,l]))