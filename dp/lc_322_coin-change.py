class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp=[0]*(amount+1)

        
        for coin in coins:
            for money in range(amount+1):
                if money-coin < 0:
                    continue
                if money==coin:
                    dp[money]=1
                else:
                    if dp[money-coin]==0:
                        continue
                    else:
                        if dp[money]!=0:
                            dp[money]=min(dp[money],dp[money-coin]+1)
                        else:
                            dp[money]=dp[money-coin]+1

        return -1 if dp[amount]==0 else dp[amount]


        class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coinChange는 dp알고리즘으로 동전 값의 총합이 amount와 일치하는
        최소 동전 갯수를 반환합니다.
        시간복잡도는 O(amount*n)입니다, n=len(coins)
        '''
        dp=[float('inf')]*(amount+1)
        dp[0]=0

        
        for coin in coins:
            for x in range(coin,amount+1):
                if dp[x-coin]!=float('inf'):
                    dp[x]=min(dp[x],dp[x-coin]+1)
                

        return dp[amount] if dp[amount]!=float('inf') else -1
                        