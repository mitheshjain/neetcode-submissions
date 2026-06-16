class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength=1
        if not nums:
            return 0
        numSet=set(nums)

        for num in numSet:
            if (num-1)  not in numSet:
                length=1
                while (num+length) in numSet:
                    length+=1
                maxLength=max(maxLength,length)
        return maxLength