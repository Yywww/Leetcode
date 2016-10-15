class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		while True:
			if len(nums1)+len(nums2)>2:
				try:
					if nums2[0]>=nums1[0]:
						nums1.pop(0)
					else:
						nums2.pop(0)
				except:
					try:
						nums1.pop(0)
					except:
						nums2.pop(0)
				try:
					if nums2[-1]>=nums1[-1]:
						nums2.pop()
					else:
						nums1.pop()
				except:
					try:
						nums1.pop()
					except:
						nums2.pop()
			else:
				break
		nums3=nums1+nums2
		if len(nums3)==1:
			return nums3[0]
		else:
			return (nums3[0]+nums3[1])/float(2)
