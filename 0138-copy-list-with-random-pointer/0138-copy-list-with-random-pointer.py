class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None

        d = {}
        temp = head

        # Create copies of all nodes
        while temp:
            d[temp] = Node(temp.val)
            temp = temp.next

        # Connect next and random pointers
        temp = head

        while temp:
            d[temp].next = d.get(temp.next)
            d[temp].random = d.get(temp.random)
            temp = temp.next

        return d[head]