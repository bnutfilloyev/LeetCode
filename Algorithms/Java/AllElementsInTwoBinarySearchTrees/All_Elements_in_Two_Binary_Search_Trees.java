class Solution {
    List<Integer> list = new ArrayList<>();
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        getAllValues(root1);
        getAllValues(root2);
        return list.stream().sorted().collect(Collectors.toList());
    }
    public void getAllValues(TreeNode root){
        if(root == null)
            return;
        list.add(root.val);
        getAllValues(root.left);
        getAllValues(root.right);
    }
}