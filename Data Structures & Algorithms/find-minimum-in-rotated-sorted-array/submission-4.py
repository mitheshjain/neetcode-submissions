class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end=0,len(nums)-1
        min=nums[start]
        while start<end:
            if nums[end]<nums[start]:
                min=nums[end]
                end-=1
            else:
                return min
        return min