class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        temp = head
        count = 0

        # Count nodes
        while temp:
            count += 1
            temp = temp.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while count >= k:
            curr = prev.next
            next_node = curr.next

            # Reverse k nodes
            for i in range(k - 1):
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = curr.next

            prev = curr
            count -= k

        return dummy.next