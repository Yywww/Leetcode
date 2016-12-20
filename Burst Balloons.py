# class Solution(object):
# 	def maxCoins(self, nums):
# 		if nums==[]:
# 			return 0
# 		if len(nums)==1:
# 			return nums[0]
# 		if len(nums)==2:
# 			return nums[0]*nums[1]+max(nums)
# 		return max([nums[i]*nums[i-1]*nums[i+1]+Solution().maxCoins(nums[:i]+nums[i+1:]) for i in range(1,len(nums)-1)]+
# 			[nums[-1]*nums[-2]+Solution().maxCoins(nums[:-1])]+
# 			[nums[0]*nums[1]+Solution().maxCoins(nums[1:])])
class Solution(object):
	def maxCoins(self, nums):
		n = len(nums)
		nums = [1] + nums + [1]
		dp = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]
		print dp
		def DP(i, j):

			if dp[i][j] > 0: return dp[i][j]
			for x in xrange(i, j + 1):
				dp[i][j] = max(dp[i][j],DP(i, x - 1) + nums[i - 1] * nums[x] * nums[j + 1]+ DP(x + 1, j))
			print dp
			return dp[i][j]
		return DP(1,n)
		
print Solution().maxCoins([3,1,5,8])