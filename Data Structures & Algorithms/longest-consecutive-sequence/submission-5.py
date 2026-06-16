class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        maxResult=1
        prev=nums[0]
        result=1
        for i in range(1,len(nums)):
            curr=nums[i]
            print(curr)
            if curr==prev:
                continue 
            if curr==prev+1:
                result+=1
                maxResult=max(maxResult,result)
            else:
                
                result=1
            prev=curr
        return maxResult