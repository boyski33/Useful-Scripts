def height(root):
    sum = 0
    if root.left:
        sum = 1 + height(root.left)
    if root.right:
        sum = 1 + height(root.right)
    
    return sum
    
