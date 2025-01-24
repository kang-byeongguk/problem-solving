import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        results=[]
        heapq.heapify(heap) #(cost,x,y)
        for x,y in points:
            cost =x*x +y*y
            heapq.heappush(heap,(cost,x,y))
        
    #추후 수정사항. heap을 max힘으로 바꾼후, heap의 갯수를 k개로 제한하기
    #->nlogk로 알고리즘 개선
        for _ in range(k):
            cost,x,y=heapq.heappop(heap)
            results.append([x,y])
        
        return results


        