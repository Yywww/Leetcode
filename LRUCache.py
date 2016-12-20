class LRUCache(object):

    def __init__(self, capacity):
        self.capacity=capacity
        self.dic_value={}
        self.list=[]

    def get(self, key):
        if key in self.dic_value:
            i=self.list.index(key)
            self.list=self.list[:i]+self.list[i+1:]+[key]
            return self.dic_value[key]
        else:
            return -1
        
    def set(self, key, value):
        if key not in self.dic_value and len(self.list)>=self.capacity:
            delkey=self.list[0]
            self.list.pop(0)
            del self.dic_value[delkey]
        self.dic_value[key]=value
        if key in self.list:
            i=self.list.index(key)
            self.list=self.list[:i]+self.list[i+1:]+[key]
        else:
            self.list.append(key)

a=LRUCache(2)
a.set(1,1)
a.set(2,3)
print a.get(2)
a.set(2,4)
print a.get(2)
a.set(3,1)
print a.get(1)