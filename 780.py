class Solution(object):
	def reachingPoints(self, sx, sy, tx, ty):
		while tx+ty>sy+sx:
			if tx>ty:
				tx -= max(ty * ((tx-sx)//ty),ty)
			elif tx<ty:
				ty -= max(tx * ((ty-sy)//tx),tx)
			elif tx==ty:
				return False
		if tx==sx and ty==sy:
			return True
		else:
			return False

print(Solution().reachingPoints(3,3,9,12))
