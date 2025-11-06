def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # 1–2. eset
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # 3. eset – két gyerek
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root
