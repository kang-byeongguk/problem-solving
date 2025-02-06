class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        '''
        canJump 함수는 주어진 nums의 마지막 인덱스에 도달가능 여부를 그리디 알고리즘으로 
        판단합니다.
        시간복잡도 O(n), n은 nums의 길이
        '''

        #현재 점프로 도달할 수 있는 가장 먼 인덱스입니다.
        curr_max=0

        for i,jump in enumerate(nums):
            #i번째 인덱스까지 점프로 도달할 수 없는 경우
            if i>curr_max:
                return False
            #기존 curr_max 보다 멀리 점프할 수 있는 경우
            if curr_max < i+jump:
                curr_max=i+jump
        return True

        
