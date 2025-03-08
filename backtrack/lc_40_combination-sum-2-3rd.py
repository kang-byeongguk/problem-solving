class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations=[]
        combination=[]
        n = len(candidates)

        def backtrack(i,sum):
            if sum==target:
                combinations.append(combination.copy())
                return
            if sum < target:
                for j in range(i,n):
                    if i<j and candidates[j]==candidates[j-1]:
                        continue
                    sum+=candidates[j]
                    combination.append(candidates[j])
                    backtrack(j+1,sum)
                    sum-=candidates[j]
                    combination.pop()
        backtrack(0,0)
        return combinations