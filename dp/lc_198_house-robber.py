class Solution:
    def rob(self, nums: List[int]) -> int:

        # dp 문제는 dp함수를 명확하게 정의해야함
        # time O(n), space O(n)
        n =len(nums)
        dp=[0]*(n)
        dp[0]=nums[0]
        if n==1:
            return dp[0]
        #dp[i]를 집이 [0..i]까지 있을때 획득할 수 있는 최대 금액
        dp[1]=max(nums[0],nums[1])

        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        
        return dp[n-1]
        