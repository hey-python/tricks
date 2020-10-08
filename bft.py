def bft(root, arr1):
    if root:
        arr = [root]

        while len(arr) > 0:
            current = arr[0]
            del arr[0]
            arr1.append(current.val)

            if current.left:
                arr.append(current.left)
            if current.right:
                arr.append(current.right)
