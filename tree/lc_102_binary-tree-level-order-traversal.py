햣# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #결과값을 반환할 리스트를 생성합니다.
        rst = []
        #현재 노드의 level을 파악하는 변수를 생성합니다.
        level=-1
        #bfs탐색을 위한 queue를 생성합니다.
        queue=deque([])
        #root 노드가 None인 경우를 고려한 예외처리 코드
        if root is None:
            return rst
        #트리의 노드와 노드의 레벨을 튜플형태로 넣어 초기화합니다.
        queue.append((root,0))
        
        #bfs코드 
        while queue:
            node,curr_level = queue.popleft()
            if curr_level!=level:
                level = curr_level
                rst.append([])
            rst[level].append(node.val)

            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))

        return rst
    
    from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        queue = deque([root])
        result=[]
    #레벨이란 변수를 없앰 len함수로 같은 레벨 노드 수를 구한 다음. 그 갯수만큼 반복함.       
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result
