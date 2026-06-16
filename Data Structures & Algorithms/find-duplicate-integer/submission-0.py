class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(0,len(nums)):
            curr=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==curr:
                    return curr
        return -1