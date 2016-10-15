class ListNode(object):
  def __init__(self, x):
      self.val = x
      self.next = None
print 'Hello!'
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        addnext=0
        resultlist=None
        while True:
            tempt=l1.val+l2.val+addnext
            if tempt>=10:
                tempt-=10
                addnext=1
            else:
                addnext=0
            if resultlist is None:
                resultlist = ListNode(tempt)
                curnode = resultlist
            else:
                nextNode = ListNode(tempt)
                curnode.next = nextNode
                curnode = curnode.next
            if l1.next is None and l2.next is None and addnext==0:
                break
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            l1=l1.next
            l2=l2.next
        return resultlist


test1=ListNode(1)
test1.next=ListNode(2)
test1.next.next=ListNode(3)

test2=ListNode(9)
test2.next=ListNode(0)
test2.next.next=ListNode(4)
test2.next.next.next=ListNode(5)
c=Solution()
c.addTwoNumbers(test1,test2)
print c.solution.val
print c.solution.next.val
print c.solution.next.next.val
print c.solution.next.next.next.val