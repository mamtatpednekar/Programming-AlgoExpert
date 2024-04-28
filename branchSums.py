# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    branchSums = []
    calculateBranchSums(root, 0 , branchSums)
    return branchSums


def calculateBranchSums(node, runningSum, branchSums):
    if node is None:
        return 
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        branchSums.append(newRunningSum)
        return 
    calculateBranchSums(node.left, newRunningSum, branchSums);
    calculateBranchSums(node.right, newRunningSum, branchSums);
