class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        xor 비트 연산자는 교환 법칙, 결합 법칙이 성립한다.
        '''
        result = 0
        for num in nums:
            result ^= num 
        return result