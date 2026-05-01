# You are given the root of a binary tree. Your task is to print the preorder traversal of the tree.


# Input Format
# The input will be provided as follows:

# The first line contains an integer N, the number of elements in the level-order traversal.
# The second line contains N integers, representing the level-order traversal of the tree. Use -1 to represent null nodes.

# Constraints
# 1 <= N <= 10^5 where N is the number of nodes in the tree.
# 1 <= Node.val <= 10^5

# Output Format
# Print the preorder traversal of the tree as a sequence of node values separated by spaces.

# Note: Do not modify or change anything inside the main function.


# Sample Input
# 7
# 3 9 20 -1 -1 15 7
# Sample Output
# 3 9 20 15 7


from collections import deque

# how to use the tree we made so a class made with val,left,right


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# custom tree build as we have to make it as not given to us


def buildTree(values):
    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        if i < len(values) and values[i] != -1:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] != -1:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root

# core preorder logic thats it ROOT _ LEFT _ RIGHT thats it


def preOrder(root, ans):
    if root == None:
        return
    ans.append(root.val)
    preOrder(root.left, ans)
    preOrder(root.right, ans)


# -------- MAIN --------
if __name__ == "__main__":
    n = int(input())  # number of vaues/lenth hai ye
    values = list(map(int, input().split()))
    root = buildTree(values)
    ans = []
    preOrder(root, ans)
    # we can also use aloop to  itr and print in the requried formaat
    # we can use hte asterik * this print(*ans ) print thesame
    for a in ans:
        print(a, end=" ")
