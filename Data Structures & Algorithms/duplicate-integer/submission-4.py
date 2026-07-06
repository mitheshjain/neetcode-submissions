class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if not nums:
            return False
        prev=nums[0]

        for i in range(1,len(nums)):
            if prev==nums[i]:
                return True
            prev=nums[i]
        return False