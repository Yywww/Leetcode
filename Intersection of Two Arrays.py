class Solution(object):
    def intersection(self, nums1, nums2):
        if nums1==[] or nums2==[]:
            return []
        result=[]
        for i in nums1:
        	if i in nums2:
        		result.append(i)
        return list(set(result))

print Solution().intersection([1],[1])