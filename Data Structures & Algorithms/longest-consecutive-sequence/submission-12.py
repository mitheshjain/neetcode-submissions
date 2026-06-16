class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        if not nums:
            return 0
        maxSub=0
        for n in nums:
            if n-1 not in nums:
                length=1
                while n+length in nums:
                    length+=1
            
                maxSub=max(length,maxSub)
        
        return maxSub
            