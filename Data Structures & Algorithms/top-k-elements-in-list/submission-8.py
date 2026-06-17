class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numList=defaultdict(int)
        res=[]
        for num in nums:
            numList[num]+=1
        heap=[]
        for num in numList.keys():
            heapq.heappush(heap,(numList[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res