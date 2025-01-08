# 2차 리팩토링코드
# in_degree는 defaultdict대신 list형태로 0으로 초기화
#이수표(선이수, 후이수 관계)를 graph로 명명
# list comprehension을 통해서 in_degree가 0인 부분을 간결하게 탐색
# src, dest, node, neighbor 그래프 용어를 사용해 간략화
#리턴할 정답은 눈에 쉽게 띄도록 result로 명명
#시간복잡도 O(numCourses + len(prerequisites)), O(v+e)

from collections import defaultdict, deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        in_degree=[0]*numCourses
        for dest,src in prerequisites:
            graph[src].append(dest)
            in_degree[dest]+=1

        queue = deque([i for i in range(numCourses) if in_degree[i]==0])
        result=[]
        while queue:
            node=queue.popleft()
            result.append(node)
            for dest in graph[node]:
                in_degree[dest]-=1
                if in_degree[dest]==0:
                    queue.append(dest)
        if len(result)==numCourses:
            return result
        return []

        
# time 24분 20초, 초안 제출 코드
# from collections import defaultdict, deque 
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         정답=[]
#         이수표=defaultdict(list)
#         in_degree=defaultdict(int)
#         for 후이수,선이수 in prerequisites:
#             in_degree[후이수]+=1
#             이수표[선이수].append(후이수)

#         courses=deque([])
#         for i in range(numCourses):
#             if in_degree[i]==0:
#                 courses.append(i)
        
 
#         while courses:
#             선이수=courses.popleft()
#             정답.append(선이수)
#             for 후이수 in 이수표[선이수]:
#                 in_degree[후이수]-=1
#                 if in_degree[후이수]==0:
#                     courses.append(후이수)

#         if len(정답)==numCourses:
#             return 정답
#         return []

        