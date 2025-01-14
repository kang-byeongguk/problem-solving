class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[0]*n
        right=[0]*n
        product=[0]*n
          
        for i in range(n):
            if i==0:
                left[i]=nums[i]
            else:
                left[i]=left[i-1]*nums[i]
        
        for i in range(n-1,-1,-1):
            if i==(n-1):
                right[i]=nums[i]
            else:
                right[i]=right[i+1]*nums[i]

        for i in range(n):
            if i==0:
                product[i]=right[i+1]
            elif i==(n-1):
                product[i]=left[i-1]
            else:
                product[i]=left[i-1]*right[i+1]
        return product
    # 모범답안
    # left[i-1], right[i+1]을 prefix, suffix로 변수 하나로 대체함
    # class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     answer = [1] * n
        
    #     # 왼쪽에서부터의 누적 곱(접두사 곱)을 answer에 저장
    #     prefix = 1
    #     for i in range(n):
    #         answer[i] = prefix
    #         prefix *= nums[i]
        
    #     # 오른쪽에서부터의 누적 곱(접미사 곱)을 answer에 곱해줌
    #     suffix = 1
    #     for i in range(n-1, -1, -1):
    #         answer[i] *= suffix
    #         suffix *= nums[i]
        
    #     return answer

        