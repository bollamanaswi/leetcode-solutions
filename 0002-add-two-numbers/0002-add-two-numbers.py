# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=ListNode(0)
        temp=d
        c=0
        while(l1 or l2 or c):
            s=c
            if l1:
                s=s+l1.val
                l1=l1.next
            if l2:
                s=s+l2.val
                l2=l2.next
            temp.next=ListNode(s%10)
            temp=temp.next
            c=s//10
        return d.next