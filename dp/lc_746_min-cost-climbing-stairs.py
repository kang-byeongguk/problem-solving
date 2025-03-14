class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        n개의 계단 중, n번째 계단에 도착하는 최소 비용을 dp알고리즘으로 구합니다.
        cost[i] 는 i번째 계단에서 i+1번 계단으로 이동하는데 필요한 비용입니다.
        Time Complexity   : O ( n )
        Space Complextity : O ( n )
        '''
        n = len(cost)
        #dp[i]는 i번째 계단에 도착하는 최소 비용
        dp=[-1]*(n+1)
        dp[0],dp[1]=0,0

        
        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

        return dp[n]
        