class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map={}
        for n in nums:
            if n in map.keys():
                return n
            map[n]=1
        return -1