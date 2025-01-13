# time O(amount * n) ,space O(amount * n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        result=[0]*(amount+1)
        result[0]=1
        for coin in coins:
            for i in range(coin,amount+1):
                result[i]=result[i]+result[i-coin]
        
        return result[amount]
            
        