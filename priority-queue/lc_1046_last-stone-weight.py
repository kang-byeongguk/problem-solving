import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones=[]
        for stone in stones:
            negative_stones.append(-stone) #max heap을 위한 negative heap
        heapq.heapify(negative_stones)

        while negative_stones:
            
            s1=heapq.heappop(negative_stones)
            
            if not negative_stones:
                return -s1
        
            s2=heapq.heappop(negative_stones)
            if s1-s2!=0:
                heapq.heappush(negative_stones,s1-s2)
        
        return 0

        