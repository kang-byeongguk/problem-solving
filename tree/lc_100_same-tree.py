# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
<<<<<<< HEAD
=======
    # time complexity O(n+m) n,m은 각각 p,q의 노드 갯 수
>>>>>>> 6b1bd444f4c75c77e349bcdddf0fc04fffecf6c0
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False

        if p.val==q.val and self.isSameTree(p.left,q.left)and self.isSameTree(p.right,q.right):
            return True
        return False