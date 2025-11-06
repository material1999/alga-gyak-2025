# Bal részfa → Gyökér → Jobb részfa
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Gyökér → Bal részfa → Jobb részfa
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Bal részfa → Jobb részfa → Gyökér
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# Példa
#        8
#       / \
#      3   10
#     / \
#    1   6

# Inorder bejárás: 1 3 6 8 10
# Preorder bejárás: 8 3 1 6 10
# Postorder bejárás: 1 6 3 10 8