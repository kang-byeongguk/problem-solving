class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        currentMaxJump=0 #현재 점프로 도달할 수 있는 최대 인덱스
        nextMaxJump=0 #다음 점프로 도달할 수 있는 최대 인덱스

        count=0
        for i in range(n-1):
            nextMaxJump=max(nextMaxJump,nums[i]+i)
            if i == currentMaxJump:
                count+=1
                currentMaxJump=nextMaxJump
        return count

        