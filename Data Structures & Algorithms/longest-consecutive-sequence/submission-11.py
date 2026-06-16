class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        maxSub=1
        for i in nums:
            sub=0

            while i-1 in nums:
                sub+=1
                i+=1
            maxSub=max(sub,maxSub)
        
        return maxSub
            