class Solution(object):
	def criticalConnections(self, n, connections):
		"""
		:type n: int
		:type connections: List[List[int]]
		:rtype: List[List[int]]
		"""
		edgeMap = {}
		for con in connections:
			if con[0] in edgeMap:
				edgeMap[con[0]].append(con[1])
			else:
				edgeMap[con[0]]=[con[1]]
			if con[1] in edgeMap:
				edgeMap[con[1]].append(con[0])
			else:
				edgeMap[con[1]]=[con[0]]
		print(edgeMap)
		res = []
		for node in range(n):
			nodeEdges = edgeMap[node]
			for i in nodeEdges:
				if not dfs(i,node,edgeMap,[],0):
					if i<node:
						edge=[i,node]
					else:
						edge=[node,i]
					if edge not in res:
						res.append(edge)
		return res

def dfs(root,target,edgeMap,visited,distance):
	if root==target and distance==1:
		return False
	if root==target:
		return True
	visited.append(root)
	for i in edgeMap[root]:
		if i in visited:
			continue
		if dfs(i,target,edgeMap,visited,distance+1):
			return True
	return False

a = Solution().criticalConnections(6,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])		
print(a)