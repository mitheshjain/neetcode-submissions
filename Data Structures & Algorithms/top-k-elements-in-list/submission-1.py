class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map={}
        res=[]
        heap=[]
        for val in nums:
            map[val]=map.get(val,0)+1
        
        for num in map.keys():
            heapq.heappush(heap,(map[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
