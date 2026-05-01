from collections import deque

# =========================
# Tree Node Definition
# =========================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # har node ke paas 3 cheeze hoti hain:
        self.val = val      # value
        self.left = left    # left child
        self.right = right  # right child


# =========================
# Build Tree from List
# =========================
def buildTree(values):
    # agar list empty hai
    if not values:
        return None

    # first element root hoga
    root = TreeNode(values[0])
    queue = deque([root])  # BFS ke liye queue
    i = 1

    # jab tak queue aur list dono chal rahe hain
    while queue and i < len(values):
        curr = queue.popleft()

        # LEFT CHILD
        if values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1

        # RIGHT CHILD
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1

    return root


# =========================
# Solution Class
# =========================
class Solution:

    def averageOfLevels(self, root):
        # agar tree empty hai
        if root is None:
            return []

        result = []  # final averages store karega
        queue = deque([root])

        # BFS (Level Order Traversal)
        while queue:
            level_sum = 0
            level_size = len(queue)

            # ek level ke saare nodes process karo
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # left child add karo
                if node.left:
                    queue.append(node.left)

                # right child add karo
                if node.right:
                    queue.append(node.right)

            # level ka average nikalo
            avg = level_sum / level_size
            result.append(avg)

        return result


# =========================
# MAIN DRIVER CODE
# =========================
if __name__ == "__main__":
    # input array (level order format)
    arr = [3, 9, 20, None, None, 15, 7]

    # tree build karo
    root = buildTree(arr)

    # solution object
    sol = Solution()

    # result print karo
    print(sol.averageOfLevels(root))
