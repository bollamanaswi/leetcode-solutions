class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        ArrayList<Integer> l = new ArrayList<>();

        if (root == null)
            return l;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int s = q.size();

            for (int i = 0; i < s; i++) {
                TreeNode node = q.poll();

                // Take the last node of each level
                if (i == s - 1)
                    l.add(node.val);

                if (node.left != null)
                    q.offer(node.left);

                if (node.right != null)
                    q.offer(node.right);
            }
        }

        return l;
    }
}