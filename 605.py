class Solution:
	def canPlaceFlowers(self, flowerbed, n):
		if n==0:
			return True
		for i,v in enumerate(flowerbed):
			if (i==0 or flowerbed[i-1]==0)  and flowerbed[i]==0 and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
				flowerbed[i]=1
				n-=1
			if n==0:
				return True
		return False


print(Solution().canPlaceFlowers([0,0,0,1],2))