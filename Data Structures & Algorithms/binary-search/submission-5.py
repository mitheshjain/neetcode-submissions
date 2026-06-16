class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end=0,len(nums)//2
        while start<=end:
            if nums[start]==target:
                return start
            if nums[end]==target:
                return end
            if target>nums[end]:
                start=end+1
                end=len(nums)-1
            else:
                start=start+1
                end=end-1
        return -1
            
            

        