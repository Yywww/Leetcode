class Solution(object):
	def catMouseGame(self, graph):
		self.graph=graph
		self.dpc = {}
		self.dpm = {}
		res = self.bfsMouse([],2,1)
		if res==0 or res==1:
			res = 1 - res
		# print(res)

		return res

	def bfsCat(self,path,cat,mouse):
		if (cat,mouse) in path:
			return 1
		if (cat,mouse) in self.dpc:
			return self.dpc[(cat,mouse)]
		children = self.graph[cat]
		maxv = 0
		for child in children:
			if child==0:
				continue
			if child==mouse:
				return 2
			val = self.bfsMouse(path+[(cat,mouse)],child,mouse)
			if val>maxv:
				maxv = val
		self.dpc[(cat,mouse)] = maxv
		return maxv
	def bfsMouse(self,path,cat,mouse):
		if (cat,mouse) in path:
			return 1
		if (cat,mouse) in self.dpm:
			return self.dpm[(cat,mouse)]
		children = self.graph[mouse]
		minv = 2
		for child in children:
			if child==cat:
				continue
			if child==0:
				return 0
			val = self.bfsCat(path+[(cat,mouse)],cat,child)
			if val<minv:
				minv = val
		self.dpm[(cat,mouse)] = minv		
		return minv

Solution().catMouseGame([[5,21,28],[6,8,9,13,23,24,30],[9,10,22,24],[24,30],[5,6,8,9,13,18,19,20,24],[0,4,9,10,11,12,22,27],[1,4,9,11,16,19,25,30],[8,9,13,19,25,26],[1,4,7,9,29],[1,2,4,5,6,7,8,13,18,19,24,26,28,29],[2,5,15,22,27,30],[5,6,12,24],[5,11,20,22,23],[1,4,7,9,29,30],[19,24,27],[10,16,19],[6,15,27],[20,22,24,29],[4,9,21],[4,6,7,9,14,15,20,26,28,30],[4,12,17,19,21],[0,18,20,27],[2,5,10,12,17],[1,12,26,30],[1,2,3,4,9,11,14,17,27,29],[6,7,26,27,29],[7,9,19,23,25],[5,10,14,16,21,24,25],[0,9,19,30],[8,9,13,17,24,25],[1,3,6,10,13,19,23,28]])