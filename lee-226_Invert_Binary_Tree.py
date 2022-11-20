class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


def print_tree(tree):
    print(tree.left.left.val, tree.right.right.val)


def main():
    item4 = TreeNode(1)
    item5 = TreeNode(3)
    item2 = TreeNode(2, item4, item5)
    item6 = TreeNode(6)
    item7 = TreeNode(9)
    item3 = TreeNode(7, item6, item7)
    item1 = TreeNode(4, item2, item3)
    print_tree(item1)
    invertTree(item1)
    print_tree(item1)


main()
