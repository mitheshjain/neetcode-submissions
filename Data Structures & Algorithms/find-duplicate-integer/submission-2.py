class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        vals=set()

        for n in nums:
            if n in vals:
                return n
            vals.add(n)
        return -1