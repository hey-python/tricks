def dft(root, arr):

    # Inorder
    if root:
        dft(root.left)
        arr.append(root.val)
        dft(root.right)
