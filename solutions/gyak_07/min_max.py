def find_min(root):
    while root.left:
        root = root.left
    return root

def find_max(root):
    while root.right:
        root = root.right
    return root
