def nodeDepths(root, sum=0):
    # Write your code here.
    currentSum = sum
    if(root.left is None and root.right is None):
        return sum 
    if(root.left is not None):
        currentSum += nodeDepths(root.left, sum + 1)
    if(root.right is not None):
        currentSum += nodeDepths(root.right, sum+1)
    return currentSum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
