class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()

        prev=nums[0]
        for n in range(1,len(nums)):
            if nums[n]==prev:
                return prev
            prev=nums[n]
        return -1