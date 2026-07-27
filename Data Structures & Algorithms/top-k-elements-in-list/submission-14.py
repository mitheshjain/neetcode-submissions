class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap={}

        for i in nums:
            freqMap[i]=freqMap.get(i,0)+1
        
        minHeap=[]

        for i in freqMap.keys():
            heapq.heappush(minHeap,(freqMap.get(i),i))

            if len(minHeap)>k:
                heapq.heappop(minHeap)
        res=[]

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res