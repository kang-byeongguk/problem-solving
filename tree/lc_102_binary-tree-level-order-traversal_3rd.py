from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        이진 트리에서 같은 레벨에 속하는 노드를 하나의 리스트에 담아
        이차원 리스트 형태로 반환하는 함수입니다.
        같은 레벨에 속할 경우 왼쪽에 위치한 노드가 먼저 리스트에 담깁니다.

        반환값예시        : [ [level 0 노드 집합], [level 1 노드 집합], ... ]
        Time complexity  : O ( n ) 단, n은 이진트리 노드 수
        Space Complexity : O ( n ) n은 이진트리 노드 수
        """
        if root is None:
            return []

        queue=deque([root])
        result = []


        # 모든 노드를 순회합니다
        while queue:
            # 같은 level에 존재하는 노드를 저장하는 리스트
            same_levels=[]
            count = len(queue) #특정 level에 존재하는 노드의 개수를 count

            for _ in range(count):
                node = queue.popleft()
                same_levels.append(node.val)

                # 자식 노드를 queue에 추가합니다
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(same_levels)
        return result
