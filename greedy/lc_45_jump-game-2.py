class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        n-1번 인덱스에 도달하기 위한 최소 점프 횟수를 반환하는 함수
        Time Complexity : O ( n )
        '''
        n = len(nums)
        count=0
        # 점프를 count 번 했을때, 도달할 수 있는 최대 인덱스
        currentMaxJump=0
        # 점프를 count + 1 번 했을 때, 도달할 수 있는 최대 인덱스 
        nextMaxJump=0 

        for i in range(n-1):
            nextMaxJump=max(nextMaxJump,nums[i]+i)
            if i == currentMaxJump:
                count+=1
                currentMaxJump=nextMaxJump
        return count

        