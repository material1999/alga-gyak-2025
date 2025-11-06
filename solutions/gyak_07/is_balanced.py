def is_balanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    return False
