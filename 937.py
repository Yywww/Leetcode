class Solution(object):
	def reorderLogFiles(self, logs):
		letter = []
		number = []
		for log in logs:
			ochar = ord(log.split(' ')[1][0])
			if ochar >= ord('0') and ochar <= ord('9'):
				number.append(log)
			else:
				letter.append(log)
		letter = sorted(letter, key = lambda x: (x.split(" ",1)[1], x.split(" ",1)[0]))
		return letter+number

ans = Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print(ans)