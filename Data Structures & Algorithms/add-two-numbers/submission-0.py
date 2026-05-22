# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listA = []
        listB = []
        curA = l1
        while curA:
            listA.append(curA.val)
            curA = curA.next
        curB = l2
        while curB:
            listB.append(curB.val)
            curB = curB.next
        listA.reverse()
        num1 = 0
        for d in listA:
            num1 = num1*10 + d
        listB.reverse()
        num2 = 0
        for d in listB:
            num2 = num2*10 + d
        tn = num1 + num2
        listR = [int(d) for d in str(tn)]
        listR.reverse()

        dummy = ListNode(0)
        res = dummy

        for d in listR:
            res.next = ListNode(d)
            res = res.next
        
        return dummy.next
        
