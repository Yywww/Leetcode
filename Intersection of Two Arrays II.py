class Solution(object):
    def intersect(self, nums1, nums2):
    	sol=[]
    	for i in nums1:
    		if i in nums2:
    			nums2.remove(i)
    			sol.append(i)
    	return sol