class Solution(object):
	def maxProfit(self, prices):
		maxprofit=0
		if prices==[]: return 0
		minp=prices[0]
		for i in prices:
			if i<minp:
				minp=i
				continue
			if (i-minp)>maxprofit:
				maxprofit=i-minp
		return maxprofit