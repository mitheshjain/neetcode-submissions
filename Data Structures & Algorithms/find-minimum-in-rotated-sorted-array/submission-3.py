class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start,end=0,len(nums)-1
        
        while start<end:
            m=start+(end-start)//2
            if nums[m]<nums[end]:
                end=m
            else:
                start=m+1
        return nums[start]