from collections import deque
import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        bfs 돌면서 모든 원소를 음으로 바꿔서 힙에 저장한다 (맥스힙)
        맥스힙 길이가 k개 이상이면 k개가 될때까지 팝한다
        마지막에 최상단 원소 음 곱해서 리턴한다

        '''
        heap=[]
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            heapq.heappush(heap,-node.val)
            while len(heap)>k:
                heapq.heappop(heap)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans=-heapq.heappop(heap)
        return ans
        