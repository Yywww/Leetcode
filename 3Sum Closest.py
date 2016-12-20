class Solution:
    def threeSumClosest(self, numbers, target):
        numbers.sort()
        ans = numbers[0]+numbers[1]+numbers[2]
        mindis=abs(ans-target)
        le=len(numbers)
        for i in range(le):
            l, r = i + 1, le - 1
            while (l < r):                    
                sum_t = numbers[l] + numbers[r] + numbers[i]-target
                
                if sum_t==0:
                    return target
                if  abs(sum_t) < mindis:
                    ans = sum_t+target
                    mindis=abs(sum_t)
                if sum_t <= 0:
                    l = l + 1
                else:
                    r = r - 1
        return ans

print Solution().threeSumClosest([0,1,2],0)
