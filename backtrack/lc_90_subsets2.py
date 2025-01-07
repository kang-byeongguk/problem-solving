class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 결과 리스트(부분집합) 초기화
        subsets=[]
        # 하나의 부분집합을 표현하는 리스트 생성
        subset=[]
        # if 문에서 중복을 확인할 수 있도록 정렬
        nums.sort()
        def backtrack(i:int):
        # 만들어진 부분집합을 결과 리스트에 추가
            subsets.append(subset.copy())
            for j in range(i,len(nums)):
        # (예)[1,2(1),2(2),2(3)]에서 [1,2(1)] 가능 [1,2(2)] 불가능
                if i<j and nums[j]==nums[j-1]:
                    continue
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
        backtrack(0)
        return subsets