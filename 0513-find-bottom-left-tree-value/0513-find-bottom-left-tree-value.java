class Solution {
    public int findBottomLeftValue(TreeNode root) {

        ArrayList<Integer> l = new ArrayList<>();

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int s = q.size();

            for (int i = 0; i < s; i++) {
                TreeNode node = q.poll();

                if (i == 0)
                    l.add(node.val);

                if (node.left != null)
                    q.offer(node.left);

                if (node.right != null)
                    q.offer(node.right);
            }
        }

        return l.get(l.size() - 1);
    }
}