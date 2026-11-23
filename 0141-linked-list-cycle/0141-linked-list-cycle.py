class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp1 = head
        temp2 = head

        while temp2 != None and temp2.next != None:
            temp1 = temp1.next
            temp2 = temp2.next.next

            if temp1 == temp2:
                return True

        return False
        