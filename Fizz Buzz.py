class Solution(object):
    def fizzBuzz(self, n):
    	solset=[]
    	for i in range(n):
    		j=i+1
    		if j%3==0:
    			if j%5==0:
    				solset.append('FizzBuzz')
    			else:
    				solset.append('Fizz')
    		elif j%5==0:
    			solset.append('Buzz')
    		else:
    			solset.append(str(i+1))
    	return solset

print Solution().fizzBuzz(20)