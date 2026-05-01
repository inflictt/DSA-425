# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ans(self, root):
        ans = []
        if root == None:
            return ans
        q = deque([root])
        # q.append()#puri ki puri node daal do taaki baad mai l and r access kr paaye hum
        # itr over q to empty dn refill it with adjacnet l and r
        while q:
            curr_level = []
            for _ in range(len(q)):
                e = q.popleft()  # now it hold the node with it
                curr_level.append(e.val)
                # the value being place to ans as it is requried first then left and right of e
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            ans.append(curr_level)
        return ans

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = self.ans(root)
        return values
