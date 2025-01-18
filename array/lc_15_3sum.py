class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort() #nlogn
        result=[]
        for i in range(n-2): #n^2
            if i>0 and nums[i]==nums[i-1]:
                continue
            start,end=i+1,n-1
            while start<end:
                if nums[i]+nums[start]+nums[end]<0:
                    start+=1
                elif nums[i]+nums[start]+nums[end]>0:
                    end-=1
                else:
                    result.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while start<n and nums[start-1]==nums[start]:
                        start+=1
        return result

# 1차 코드풀이.
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
            
#             j = i + 1
#             k = len(nums) - 1

#             while j < k:
#                 total = nums[i] + nums[j] + nums[k]

#                 if total > 0:
#                     k -= 1
#                 elif total < 0:
#                     j += 1
#                 else:
#                     res.append([nums[i], nums[j], nums[k]])
#                     j += 1

#                     while nums[j] == nums[j-1] and j < k:
#                         j += 1
        
#         return res
        



        