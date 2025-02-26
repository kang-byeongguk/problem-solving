class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        주어진 stock 가격 배열에서 한 번의 매수와 매도로 얻을 수 있는 최대 이익을 구합니다.
        매수는 반드시 매도보다 앞서야 합니다.

        Time complexity  : O ( n )  단, n 은 len(prices)
        Space complexity : O ( 1 )
        """
        max_profit=0 #최대 이익
        min_price=float('inf') #stock의 최저 가격

        for price in prices:
            # 기존보다 저렴한 가격을 찾으면 최저 가격을 갱신합니다.
            if price < min_price:
                min_price=price
            # 기존보다 높은 이익을 구할 수 있으면 최대 이익을 갱신합니다.
            curr_profit= price - min_price
            max_profit = max(max_profit,curr_profit)

        return max_profit