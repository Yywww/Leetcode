
def generalizedGCD(num, arr):
    
    if len(arr)==1:
        return arr[0]
    while True:
        newArr = []
        curMin = min(arr)
        for i in arr:
            if i%curMin!=0:
                newArr.append(i%curMin)
        if len(newArr)==0:
            return curMin
        arr = newArr
        print(arr)
    return curMin

print(generalizedGCD(5,[11,13,15,17,19]))