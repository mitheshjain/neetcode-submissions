class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        slow,fast=nums[0],nums[0]
        i=0
        if slow==target:
            return 0
        
        for i in range(len(nums)-1):
            i=i+1
            slow=nums[i]
            if i<len(nums)-1:
                fast=nums[i+1]
            if fast==target:
                return i+1
            elif slow==target:
                return i
            
        return -1