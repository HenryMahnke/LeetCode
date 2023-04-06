# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pArray = self.top_down(p)
        print(pArray)
        qArray = self.top_down(q)
        print(qArray)
        return pArray == qArray

    def top_down(self, node):
        if node is None:
            return [None]
        results = []
        results.append(node.val)
        results.extend(self.top_down(node.left))
        results.extend(self.top_down(node.right))
        return results