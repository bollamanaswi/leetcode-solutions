class Solution {
    public int findBottomLeftValue(TreeNode root) {

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        int ans = 0;

        while (!q.isEmpty()) {
            int s = q.size();

            for (int i = 0; i < s; i++) {
                TreeNode node = q.poll();

                // First node of each level
                if (i == 0)
                    ans = node.val;

                if (node.left != null)
                    q.offer(node.left);

                if (node.right != null)
                    q.offer(node.right);
            }
        }

        return ans;
    }
}