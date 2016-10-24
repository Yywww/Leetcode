class Solution(object):
    def majorityElement(self, nums):
    	l=len(nums)/2
        for i in list(set(nums)):
        	if nums.count(i)>l:
        		return i