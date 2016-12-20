class Solution(object):
	def fullJustify(self, words, maxWidth):
		length=0
		curline_word=[]
		result=[]
		# if words==['']:
		# 	return [' '*maxWidth]
		for i in words:
			if length==0:
				length+=len(i)
			else:
				length+=len(i)+1
			if length>maxWidth:
				if len(curline_word)==1:
					curline=curline_word[0]+' '*(maxWidth-len(curline_word[0]))
				else:	
					wordlen=sum([len(j) for j in curline_word])
					space=maxWidth-wordlen
					spaceper=space/(len(curline_word)-1)
					nm=space-spaceper*(len(curline_word)-1)
					print nm
					curline=''
					for j in range(len(curline_word)):
						curline+=curline_word[j]
						if j==len(curline_word)-1:
							continue
						if j<nm:
							curline+=' '*(spaceper+1)
						else:
							curline+=' '*spaceper
				print curline
				result.append(curline)
				curline_word=[i]
				length=len(i)
			else:
				curline_word.append(i)
			if i==words[-1]:
				curline=''
				for j in range(len(curline_word)):
					curline+=curline_word[j]
					if j==len(curline_word)-1:
						curline+=' '*(maxWidth-len(curline))
						continue
					curline+=' '
				print curline
				result.append(curline)
		return result
print Solution().fullJustify([""],2)
