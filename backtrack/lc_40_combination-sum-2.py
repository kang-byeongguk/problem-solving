class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        results=[]
        result=[]

    
        def backtrack(index,total):
            

            result.append(candidates[index])
            total+=candidates[index]
            if total == target:
                results.append(result.copy())

            if total < target:
                for j in range(index+1,n):
                    if candidates[j-1]!=candidates[j] or j==index+1:
                        backtrack(j,total)
            
            result.pop()
            total-=candidates[index]
        
            





        for i in range(n):
            if i!=0 and candidates[i-1]==candidates[i]:
                continue;
            backtrack(i,0)
        return results

## 첨삭 후 수정. 호출을 for문 안쓰고 간략하게. 대신 함수 시작에서 종료 여부를 판별
## index, i,j를 start, i로 변경
# if 문으로 중복여부 체크할때 start<i조건으로 변경   
    class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        results=[]
        result=[]

    
        def backtrack(start,curr_sum):

            if curr_sum == target:
                results.append(result.copy())
                return
            elif curr_sum > target:
                return

            
            for i in range(start,n):
                if start < i and candidates[i-1]==candidates[i]:
                    continue
                result.append(candidates[i])
                curr_sum+=candidates[i]
                backtrack(i+1,curr_sum)
                result.pop()
                curr_sum-=candidates[i]
            

        backtrack(0,0)
        return results

            

