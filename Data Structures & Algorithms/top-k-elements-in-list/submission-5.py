class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numList={}
        for n in nums:
            numList[n]=numList.get(n,0)+1
        heap=[]

        for num in numList.keys():
            heapq.heappush(heap,(numList[num],num))
            if len(heap)> k:
                heapq.heappop(heap)
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        