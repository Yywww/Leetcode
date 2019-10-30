class Solution(object):
    def shortestSubarray(self, A, K):
    	Asum = []
    	s = 0
    	for i in A:
    		s+=i
    		Asum.append(s)
    	
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """