class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total=sum(gas)-sum(cost)
        if total<0:
            return -1
        tank=0 #현재 인덱스에서 다음 인덱스로 넘아 갈 수 있는지 정의
        start=0 #탱크가 0인 상태에서 처음으로 출발하는 인덱스
        for i in range(n):
            tank+=gas[i]-cost[i]
            if tank < 0:
                start=i+1
                tank = 0
        return -1 if start==n else start
