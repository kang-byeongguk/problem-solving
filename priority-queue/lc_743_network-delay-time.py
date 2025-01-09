from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)  # 인접리스트 생성을 위한 딕셔너리 생성
        costs=[float('inf') for _ in range(n+1)]  # costs[i]는 i번 노드를 방문하는데 걸리는 시간
        costs[0]=-1 #0번 노드는 존재하지 않음

        # 인접리스트 생성
        for u,v,w in times:
            graph[u].append((v,w))

        # (cost,node) initialization
        #  우선순위 큐를 위한 heap 생성
        heapq.heappush(heap,(0,k))

        #다익스트라 알고리즘
        while heap:
            cost,u=heapq.heappop(heap)
            if cost<costs[u]:
                costs[u]=cost
                for v,w in graph[u]:
                    heapq.heappush(heap,(w+cost,v))
                    
        # 미방문 노드가 존재하면 -1를 리턴, 존재하지 않는 경우 마지막 노드의 방문 시간을 리턴
        for i in range(1,n+1):
            if costs[i]==float('inf'):
                return -1
            
        return max(costs[1:])
        
            
        


        