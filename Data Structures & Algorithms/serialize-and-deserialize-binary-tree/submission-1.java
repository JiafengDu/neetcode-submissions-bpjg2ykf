/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serializeHelper(root, sb);
        return sb.toString();
    }

    private void serializeHelper(TreeNode node, StringBuilder sb) {
        if (node==null) {
            sb.append("N,");
            return;
        }
        sb.append(node.val).append(",");
        serializeHelper(node.left, sb);
        serializeHelper(node.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] tokens = data.split(",");
        int[] idx = new int[]{0};
        return deserializeHelper(tokens, idx);
    }

    private TreeNode deserializeHelper(String[] tokens, int[] idx) {
        String token = tokens[idx[0]++];
        if (token.equals("N")) {
            return null;
        }

        TreeNode node = new TreeNode(Integer.parseInt(token));
        node.left = deserializeHelper(tokens, idx);
        node.right = deserializeHelper(tokens, idx);
        return node;
    }
}
