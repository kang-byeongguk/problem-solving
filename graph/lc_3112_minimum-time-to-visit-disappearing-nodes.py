from collections import defaultdict
import heapq
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

        # 다익스트라로 해결
        times=[float('inf')]*n
        # 모든 배열의 시간을 리스트로 저장하기 초반에는 무한대로 설정
        # 양방향이니까 디폴트딕트 u,v 각각 채우기
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))


        heap=[(0,0)]
        times[0]=0
        # 힙을 설정하고 초반노드 (시간,노드) 추가

        # 힙 반복
        while heap:
        # 힙에서 노드 꺼낸후 인접 노드 들 최소화 할 수 있는지 탐색하는데
        # 조건이 2개 있음
        # 현재 노드 사라졌으면  컨티뉴
        # 시간 더 못 줄이면 컨티뉴
            time,node=heapq.heappop(heap)
            if time>=disappear[node]:
                continue
            if time > times[node]:
                continue
        # 인접 노드 탐색 후 줄일 수 있으면 줄이고 줄인거 힙에 ?
            for neighbor,w in graph[node]:
                arrival=w+time
                if arrival>=disappear[neighbor]:
                    continue
                if times[neighbor]>arrival:
                    times[neighbor]=arrival
                    heapq.heappush(heap,(arrival,neighbor))
            
        # 모든 times 중에서 시간이 disappear보다 갖거나 크면 -1 아니면 times

        for node in range(n):
            if times[node]>=disappear[node]:
                times[node]=-1
        return times

