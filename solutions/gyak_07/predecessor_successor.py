def successor(root):
    return find_min(root.right) if root and root.right else None

def predecessor(root):
    return find_max(root.left) if root and root.left else None
