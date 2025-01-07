from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        freq=defaultdict(int)
        # 1.숫자의 빈도수 계산
        for num in nums:
            freq[num]+=1
        # 2. 결과 리스트(부분집합) 초기화
        subsets=[[]]
        # 3. 각 고유 숫자와 등장 횟수에 대해
        for num, count in freq.items():
            new_subsets=[]
        # 4. (예) count가 2라면 num 1개 추가했을 때와 2개를 추가했을 때 모두 고려
        # 모든 count와 모든 subset을 연산함
            for c in range(1,count+1):
                for subset in subsets:
        # 5. (예) subset이 [1,2] num이 3 c가 2라면 [1,2,3,3]
                    new_subsets.append(subset+[num]*c)
        # 6. 기존 부분집합에 새로운 부분집합을 이어붙인다.
            subsets+=new_subsets

        return subsets
        