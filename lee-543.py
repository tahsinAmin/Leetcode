def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    max_value = [0]
    def dfs(root):
        if root:
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            max_value[0] = max(max_value[0], left_height + right_height + 2)

            return 1 + max(left_height, right_height)
        else:
            return -1
    
    dfs(root)
    return max_value[0]