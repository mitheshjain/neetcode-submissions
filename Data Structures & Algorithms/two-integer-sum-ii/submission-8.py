class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end=0,len(numbers)-1

        while start<end:
            sumValue=numbers[start]+numbers[end]
            if sumValue==target:
                return [start+1,end+1]
            elif sumValue>target:
                end-=1
            else:
                start+=1
        return []