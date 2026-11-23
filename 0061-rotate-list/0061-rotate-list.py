class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head

        # Find the length of the linked list
        temp = head
        length = 1

        while temp.next is not None:
            temp = temp.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Connect the last node to the first node
        temp.next = head

        # Find the new last node
        steps = length - k
        temp = head

        for i in range(steps - 1):
            temp = temp.next

        # Set the new head
        new_head = temp.next

        # Break the circular linked list
        temp.next = None

        return new_head