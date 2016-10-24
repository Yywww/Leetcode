class Solution(object):
	def readBinaryWatch(self, num):
		comb=[[]]
		for i in range(10):
			temp=[]
			for r in comb:
				if r.count(1)<num:
					if num-r.count(1)==10-i:
						temp.append(r+[1])
					else:
						temp.append(r+[0])
						temp.append(r+[1])
				if r.count(1)==num:
					temp.append(r+[0])
			comb=temp
		sol=[]
		for i in comb:
			minute=i[4]*32+i[5]*16+i[6]*8+i[7]*4+i[8]*2+i[9]*1
			hour=i[0]*8+i[1]*4+i[2]*2+i[3]*1
			if minute<60 and hour<12:
				if minute<10:
					sol.append(str(hour)+":0"+str(minute))
				else:
					sol.append(str(hour)+":"+str(minute))
		return sol


print Solution().readBinaryWatch(2)
