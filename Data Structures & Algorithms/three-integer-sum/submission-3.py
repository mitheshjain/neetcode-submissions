class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        start=0

        res=[]

        for i,a in enumerate(nums):
            if a>0:
                break
            
            if nums[i-1]==a and i>0:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                currSum=a+nums[l]+nums[r]
                if currSum>0:
                    r-=1
                elif currSum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l-1]==nums[l]:
                        l+=1
        return res