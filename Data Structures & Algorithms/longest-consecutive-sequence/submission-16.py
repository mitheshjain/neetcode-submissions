class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen=set(nums)
        res=0
        for i in seen:

            if i-1 not in seen:
                start=1
                while i+start in seen:
                    start+=1
                res=max(start,res)
                
        return res