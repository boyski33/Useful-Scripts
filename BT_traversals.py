# preorder
def preOrder(root):
    print(root.data)
    if root.left:
        preOrder(root.left)
    # print(root.data) #inorder
    if root.right:
        preOrder(root.right)

    # print(root.data) #postorder

