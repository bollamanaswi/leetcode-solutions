from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        q = deque([root])
        r = []

        while q:
            level = []

            for p in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            r.append(level)

        return r[::-1]