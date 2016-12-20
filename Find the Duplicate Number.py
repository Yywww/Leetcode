class Solution(object):
	def findDuplicate(self, nums):
		slow = 0
		fast = 0
	
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			print slow,fast
			if slow == fast:
				break
	
		finder = 0
		while True:
			slow   = nums[slow]
			finder = nums[finder]

			if slow == finder:
				return slow
print Solution().findDuplicate([5,1,2,3,6,4,5])